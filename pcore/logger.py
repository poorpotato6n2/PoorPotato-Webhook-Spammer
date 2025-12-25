from colorama import Fore
from datetime import datetime
import threading

class Logger:
    lock = threading.Lock()

    @staticmethod
    def _print(prefix, color, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        with Logger.lock:
            print(f"{Fore.LIGHTBLACK_EX}[{timestamp}] {color}[{prefix}] {Fore.RESET}{message}")

    @staticmethod
    def info(msg):
        Logger._print("INFO", Fore.CYAN, msg)

    @staticmethod
    def success(msg):
        Logger._print("SENT", Fore.GREEN, msg)

    @staticmethod
    def error(msg):
        Logger._print("FAIL", Fore.RED, msg)
        
    @staticmethod
    def warn(msg):
        Logger._print("WARN", Fore.MAGENTA, msg)
        
    @staticmethod
    def rate_limit(msg):
        Logger._print("RATE", Fore.YELLOW, msg)