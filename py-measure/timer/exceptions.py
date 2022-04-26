class TimerError(Exception):
    def __init__(self, message="An error ocurred with the timer.") -> None:
        self.message = message
        super().__init__(self.message)
