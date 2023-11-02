import PyInstaller.__main__
from src.config import SCRIPT


PyInstaller.__main__.run([
    SCRIPT,                             # Ruta al script principal
    '--onefile',                        # Compilar a un solo archivo
    '--windowed',                       # Modo ventana (sin consola)
    '--name=spellsolver',               # Nombre del ejecutable
    '--add-data=assets;assets',         # Incluir directorio assets (cambiar ; por : en Linux/Mac)
    '--distpath=dist',                  # Directorio de salida
    '--workpath=build',                 # Directorio de trabajo
    '--noconfirm',                      # Sobrescribir sin preguntar
    '--icon=assets/spellsolver.ico',    # Icono del ejecutable
    #'--debug=all',                      # Información de depuración
    '--clean',                          # Limpiar archivos temporales
])
