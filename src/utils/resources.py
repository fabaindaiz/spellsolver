import os
import sys


def resource_path(relative_path: str) -> str:
    """Obtener la ruta absoluta al recurso en el sistema de archivos."""
    try:
        # PyInstaller crea un archivo temporal y lo coloca en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)
