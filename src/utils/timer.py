from datetime import datetime


class Timer:
    """Represents a timer taht can measure elapsed times"""

    def __init__(self) -> None:
        self.reset_timer()

    def reset_timer(self) -> None:
        """Reset starting time to now"""
        self.start_time = datetime.now()

    def elapsed_seconds(self) -> float:
        """Get elapsed time in seconds"""
        end_time = datetime.now()
        elapsed_time = (end_time - self.start_time).total_seconds()
        return round(elapsed_time, 2)

    def elapsed_millis(self) -> float:
        """Get elapsed time in milliseconds"""
        end_time = datetime.now()
        elapsed_time = (end_time - self.start_time).total_seconds() * 1000
        return round(elapsed_time, 0)
