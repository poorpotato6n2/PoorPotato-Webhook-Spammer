import random
import time
import httpx
from itertools import cycle
from .logger import Logger
from .utils import format_proxy
from .stats import Statistics

class PoorPotatoEngine:
    def __init__(self, config, webhooks, messages, proxies):
        self.config = config
        self.webhooks = webhooks
        self.messages = messages
        self.proxies = proxies
        self.proxy_cycle = cycle(self.proxies) if self.proxies else None
        self.log_cfg = config.get('logging', {})
        self.headers = {"User-Agent": config.get("user_agent", "PoorPotato")}
        self.http2_enabled = self.config.get('http2_enabled', False)
        self.ping_everyone = config.get('ping_everyone', False)

    def get_proxy_url(self):
        if not self.config['use_proxies'] or not self.proxies:
            return None
        raw_proxy = next(self.proxy_cycle)
        return format_proxy(raw_proxy)

    def worker(self):
        use_http2 = self.http2_enabled
        
        while True:
            proxy_url = self.get_proxy_url()
            
            limits = httpx.Limits(
                max_keepalive_connections=None, 
                max_connections=None, 
                keepalive_expiry=None
            )
            
            try:
                with httpx.Client(
                    proxy=proxy_url, 
                    http2=use_http2,
                    timeout=httpx.Timeout(
                        connect=self.config.get('connect_timeout', 20.0), 
                        read=self.config.get('read_timeout', 20.0),
                        write=self.config.get('write_timeout', 20.0),
                        pool=self.config.get('pool_timeout', 20.0)
                    ),
                    headers=self.headers,
                    limits=limits,
                    verify=False
                ) as client:
                    
                    while True:
                        webhook = random.choice(self.webhooks)
                        base_message = random.choice(self.messages)
                        
                        if self.ping_everyone:
                            message = f"@everyone {base_message}"
                        else:
                            message = base_message
                        
                        payload = {"content": message}
                        
                        try:
                            response = client.post(webhook, json=payload)
                            
                            if 200 <= response.status_code < 300:
                                Statistics.add_sent()
                                if self.log_cfg.get('show_success', True):
                                    Logger.success(f"Sent to ...{webhook[-5:]}")
                            
                            elif response.status_code == 429:
                                Statistics.add_ratelimit()
                                if self.log_cfg.get('show_ratelimits', True):
                                    Logger.rate_limit("Rate Limited")
                                time.sleep(self.config['retry_interval'])
                                
                            else:
                                Statistics.add_failed()
                                if self.log_cfg.get('show_errors', False):
                                    Logger.error(f"Status: {response.status_code}")
                                
                        except Exception:
                            Statistics.add_error()
                            if self.log_cfg.get('show_errors', False):
                                pass
                            
                            if not self.config['keep_alive']:
                                break
                                
                        if self.config['sleep_interval'] > 0:
                            time.sleep(self.config['sleep_interval'])
                            
            except Exception as e:
                Statistics.add_error()
                
                err_str = str(e).lower()
                if use_http2 and ("http2" in err_str or "h2" in err_str or "initialization" in err_str):
                    use_http2 = False
                    time.sleep(1)
                    continue

                if self.log_cfg.get('show_errors', True):
                    Logger.error(f"Client Error: {e}")
                
                time.sleep(self.config['retry_interval'])