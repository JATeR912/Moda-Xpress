#10.Crear un backup del inventario: Guardar una copia de seguridad del inventario en un archivo separado.
def backup():
    import shutil
    from datetime import datetime

    try:
        ahora = datetime.now()
        fecha_hora = ahora.strftime("%Y-%m-%d_%H-%M-%S")
        nombre_backup = f"copiaseguridad_{fecha_hora}.txt"
        shutil.copy("inventario.txt", nombre_backup)
        print("Copia de seguridad creada exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al crear la copia de seguridad: {e}")

    print()