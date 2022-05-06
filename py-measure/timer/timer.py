import time
from datetime import date, datetime, timedelta
from typing import Any
from .exceptions import TimerError

PRECISION = 100000

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        if self.start_time is not None:
            raise TimerError("Timer is currently running. Use stop() to stop it.")

        self.start_time = time.perf_counter()

    def format_message(self, ms):
        date = datetime.utcfromtimestamp(ms)

        hours = f"{date.hour} hours" if date.hour else ""
        minutes = f"{date.minute} minutes" if date.minute else ""
        seconds = f"{date.second} seconds" if date.second else ""
        
        ms = int((date.timestamp() % 1) * PRECISION)
        milliseonds = f"and {ms} milliseconds" if ms else ""

        print(f"{hours} {minutes} {seconds} {milliseonds}".strip())

    def stop(self):
        if self.start_time is None:
            raise TimerError("Timer is not running. Use start() to start it.")

        elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None

        self.format_message(elapsed_time)
