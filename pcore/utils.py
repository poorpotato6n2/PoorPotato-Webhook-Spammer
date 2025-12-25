import json
import os
from urllib.parse import quote_plus

def load_config():
    default_config = {
        "threads": 200,
        "connect_timeout": 20.0,
        "read_timeout": 20.0,
        "write_timeout": 20.0,
        "pool_timeout": 20.0,
        "sleep_interval": 0.0,
        "retry_interval": 1.0,
        "ping_everyone": True,
        "use_proxies": False,
        "http2_enabled": False,
        "keep_alive": True,
        "randomize_order": True,
        "user_agent": "PoorPotato/1.0",
        "logging": {
            "show_success": True,
            "show_errors": True,
            "show_ratelimits": True
        }
    }
    
    if not os.path.exists('config.json'):
        return default_config
        
    with open('config.json', 'r') as f:
        loaded = json.load(f)
        if 'logging' in loaded: default_config['logging'].update(loaded['logging'])
        default_config.update({k: v for k, v in loaded.items() if k not in ['logging']})
        return default_config

def load_lines(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        return [line.strip() for line in f if line.strip()]

def format_proxy(proxy_str):
    parts = proxy_str.split(':')
    if len(parts) == 4:
        ip, port, user, pwd = parts[0], parts[1], parts[2], parts[3]
        user = quote_plus(user)
        pwd = quote_plus(pwd)
        return f"http://{user}:{pwd}@{ip}:{port}"
    elif len(parts) == 2:
        return f"http://{parts[0]}:{parts[1]}"
    
    if not proxy_str.startswith("http"):
        return f"http://{proxy_str}"
    return proxy_str