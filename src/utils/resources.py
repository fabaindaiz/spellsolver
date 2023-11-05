import os
import sys


def resource_path(relative_path: str) -> str:
    """
    Get the absolute path to a resource file located relative to the application executable.

    Args:
        relative_path (str): The relative path to the resource file.

    Returns:
        str: The absolute path to the resource file.
    """
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))

    return os.path.join(base_path, relative_path)
