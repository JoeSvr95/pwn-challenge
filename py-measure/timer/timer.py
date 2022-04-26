import time
from datetime import date, datetime
from typing import Any
from .exceptions import TimerError


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        if self.start_time is not None:
            raise TimerError("Timer is currently running. Use stop() to stop it.")

        self.start_time = time.perf_counter()

    def stop(self):
        if self.start_time is None:
            raise TimerError("Timer is not running. Use start() to start it.")

        elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None

        date = datetime.utcfromtimestamp(elapsed_time)
        formated = datetime.strftime(
            date, "%H hours %M minutes %S seconds %f miliseconds"
        )
        print(f"Elapsed time: {formated}")
