import PyInstaller.__main__

PyInstaller.__main__.run([
    'graphicalui.py',               # Ruta al script principal
    '--onefile',                    # Compilar a un solo archivo
    #'--windowed',                   # Modo ventana (sin consola)
    '--name=spellsolver',           # Nombre del ejecutable
    '--add-data=assets;assets',     # Incluir directorio assets (cambiar ; por : en Linux/Mac)
    '--distpath=dist',              # Directorio de salida
    '--workpath=build',             # Directorio de trabajo
    '--noconfirm',                  # Sobrescribir sin preguntar
    #'--icon=icono.ico',             # Icono del ejecutable (opcional)
    #'--debug=all',                  # Información de depuración
])
