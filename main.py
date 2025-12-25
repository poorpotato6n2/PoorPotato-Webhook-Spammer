import sys
import time
import threading
import ctypes
import os
from colorama import Fore
from pcore.branding import get_banner
from pcore.logger import Logger
from pcore.utils import load_config, load_lines
from pcore.engine import PoorPotatoEngine
from pcore.stats import Statistics

def title_worker():
    while True:
        try:
            title = (
                f"PoorPotato Webhook Spammer | "
                f"Sent: {Statistics.sent} | "
                f"Failed: {Statistics.failed} | "
                f"Rate Limited: {Statistics.ratelimit} | "
                f"Errors: {Statistics.errors}"
            )
            if os.name == 'nt':
                ctypes.windll.kernel32.SetConsoleTitleW(title)
            time.sleep(0.1)
        except:
            pass

def main():
    config = load_config()
    
    threading.Thread(target=title_worker, daemon=True).start()
    
    print(get_banner())
    
    webhooks = load_lines("webhooks.txt")
    messages = load_lines("messages.txt")
    proxies = load_lines("proxies.txt") if config['use_proxies'] else []
    
    if not webhooks:
        Logger.error("No webhooks found in webhooks.txt")
        sys.exit()
    
    if not messages:
        Logger.error("No messages found in messages.txt")
        sys.exit()

    Logger.info(f"Loaded {len(webhooks)} webhooks")
    Logger.info(f"Loaded {len(messages)} messages")
    
    if config['use_proxies']:
        Logger.info(f"Loaded {len(proxies)} proxies")
        if len(proxies) == 0:
            Logger.warn("Use Proxies is ON but proxies.txt is empty! Running proxyless might be risky.")
    
    engine = PoorPotatoEngine(config, webhooks, messages, proxies)
    
    threads = []
    for _ in range(config['threads']):
        t = threading.Thread(target=engine.worker)
        t.daemon = True
        threads.append(t)
        t.start()
    
    Logger.info(f"Started {config['threads']} threads (Stability Mode)")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}───────────────── STATISTICS ─────────────────{Fore.RESET}")
        print(f"{Fore.GREEN} Sent        : {Statistics.sent}{Fore.RESET}")
        print(f"{Fore.RED} Failed      : {Statistics.failed}{Fore.RESET}")
        print(f"{Fore.YELLOW} Rate Limited: {Statistics.ratelimit}{Fore.RESET}")
        print(f"{Fore.RED} Errors      : {Statistics.errors}{Fore.RESET}")
        print(f"{Fore.CYAN}───────────────────────────────────────────────{Fore.RESET}")
        Logger.info("Exiting...")
        sys.exit()

if __name__ == "__main__":
    main()