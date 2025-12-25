import threading

class Statistics:
    sent = 0
    failed = 0
    ratelimit = 0
    errors = 0
    _lock = threading.Lock()

    @staticmethod
    def add_sent():
        with Statistics._lock:
            Statistics.sent += 1

    @staticmethod
    def add_failed():
        with Statistics._lock:
            Statistics.failed += 1

    @staticmethod
    def add_ratelimit():
        with Statistics._lock:
            Statistics.ratelimit += 1
            
    @staticmethod
    def add_error():
        with Statistics._lock:
            Statistics.errors += 1