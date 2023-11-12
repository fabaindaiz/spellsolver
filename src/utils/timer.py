from datetime import datetime, timedelta


class Timer:
    """Represents a timer that can measure elapsed times.

    This class provides functionality to measure elapsed time intervals using various time units.
    It can be used to benchmark or profile code execution durations.

    Attributes:
        _start_time (datetime): The starting time of the timer.
    """

    def __init__(self) -> None:
        """Initialize a Timer instance.

        Sets the initial starting time of the timer to the current time.
        """
        self._start_time = None
        self.reset_timer()

    def reset_timer(self) -> None:
        """Reset the timer's starting time.

        Sets the starting time of the timer to the current time.
        """
        self._start_time = datetime.now()

    def _calculate_elapsed_time(self, time_unit) -> float:
        """Calculate elapsed time in the specified time unit.

        Args:
            time_unit (dict): A dictionary specifying the time unit to convert to.
                Example: {"seconds": 1} for seconds, {"milliseconds": 1} for milliseconds.

        Returns:
            float: The elapsed time in the specified time unit.
        """
        return (datetime.now() - self._start_time) / timedelta(**time_unit)

    @property
    def elapsed_seconds(self) -> float:
        """Get the elapsed time in seconds.

        Returns:
            float: The elapsed time in seconds, rounded to 2 decimal places.
        """
        elapsed_time = self._calculate_elapsed_time({"seconds": 1})
        return round(elapsed_time, 2)

    @property
    def elapsed_millis(self) -> float:
        """Get the elapsed time in milliseconds.

        Returns:
            float: The elapsed time in milliseconds, rounded to the nearest integer.
        """
        elapsed_time = self._calculate_elapsed_time({"milliseconds": 1})
        return round(elapsed_time, 0)
