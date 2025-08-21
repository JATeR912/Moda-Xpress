#5.Obtener atributos del archivo: Ver información sobre el archivo como el tamaño y la fecha de última modificación.
import os
from pathlib import Path
import time
def propiedades_inventario():
    directorio = Path(".")
    archivos = [f.name for f in directorio.iterdir() if f.is_file() and f.suffix == ".txt"]
    if not archivos:
        print("No hay archivos para mostrar en el directorio actual.")
        return
    print("Archivos disponibles:")
    for archivo in archivos:
        print("-", archivo)
    archivo_inventario = input("\nIngrese el nombre del archivo del que desea conocer las propiedades(con la extension .txt): ").strip()
    try:
        with open(archivo_inventario, "r", encoding="utf-8") as file:
            print("\nPropiedades del archivo:")
            print(f"Nombre: {archivo_inventario}")
            info = os.stat(archivo_inventario)
            print(f"Tamaño: {info.st_size} bytes")
            tiempo = time.ctime(info.st_mtime)
            print(f"Última modificación: {tiempo}")
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrio un error al leer el archivo: {e}")
    print()