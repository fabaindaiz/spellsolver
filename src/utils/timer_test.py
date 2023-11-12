import unittest
from datetime import datetime
from unittest.mock import patch

from .timer import Timer


class TestTimer(unittest.TestCase):
    @patch("timer.datetime")
    def test_reset_timer(self, mock_datetime):
        mock_now = datetime(2023, 8, 9, 12, 0, 0)  # Example datetime for mocking
        mock_datetime.now.return_value = mock_now

        timer = Timer()
        timer.reset_timer()

        self.assertEqual(timer._start_time, mock_now)

    @patch("timer.datetime")
    def test_elapsed_seconds(self, mock_datetime):
        mock_start_time = datetime(2023, 8, 9, 12, 0, 0)  # Example datetime for mocking
        mock_current_time = datetime(2023, 8, 9, 12, 0, 10)  # Elapsed time: 10 seconds
        mock_datetime.now.side_effect = [mock_start_time, mock_current_time]

        timer = Timer()
        elapsed_seconds = timer.elapsed_seconds

        self.assertEqual(elapsed_seconds, 10.00)

    @patch("timer.datetime")
    def test_elapsed_millis(self, mock_datetime):
        mock_start_time = datetime(2023, 8, 9, 12, 0, 0)  # Example datetime for mocking
        mock_current_time = datetime(
            2023, 8, 9, 12, 0, 0, 500000
        )  # Elapsed time: 0.5 seconds
        mock_datetime.now.side_effect = [mock_start_time, mock_current_time]

        timer = Timer()
        elapsed_millis = timer.elapsed_millis

        self.assertEqual(elapsed_millis, 500.0)


if __name__ == "__main__":
    unittest.main()
