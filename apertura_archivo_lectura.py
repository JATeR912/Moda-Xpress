#1.Apertura de archivo en modo lectura: Leer todo el inventario.
from pathlib import Path
def mostrar_inventario():
    print("--Mostrar inventario completo--")
    directorio = Path(".")
    archivos = [f.name for f in directorio.iterdir() if f.is_file() and f.suffix == ".txt"]
    if not archivos:
        print("No hay archivos en el directorio actual.")
        return
    print("Archivos disponibles:")
    for archivo in archivos:
        print("-", archivo)
    archivo_inventario = input("\nIngrese el nombre del archivo que desea leer(con la extension): ").strip()
    try:
        with open(archivo_inventario, "r", encoding="utf-8") as file:    
            contenido_inventario = file.read()
            if contenido_inventario:
                print("\nContenido del inventario:\n")
                print(contenido_inventario)
            else:
                print("El archivo está vacío.")
            print()
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    print()

