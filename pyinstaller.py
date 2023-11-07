import os

import PyInstaller.__main__

from src.config import SCRIPT


def run_pyinstaller(script_path):
    separator = os.pathsep

    options = [
        script_path,  # Path to the main script
        "--onefile",  # Compile to a single file
        "--windowed",  # Windowed mode (no console)
        "--name=spellsolver",  # Executable name
        f"--add-data=assets{separator}assets",  # Include the 'assets' directory
        "--distpath=dist",  # Output directory
        "--workpath=build",  # Working directory
        "--noconfirm",  # Overwrite without asking for confirmation
        "--icon=assets/spellsolver.ico",  # Icon for the executable
        "--clean",  # Clean temporary files after building
    ]

    PyInstaller.__main__.run(options)


if __name__ == "__main__":
    run_pyinstaller(SCRIPT)
