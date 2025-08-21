#6.Leer un producto específico: Buscar por nombre o ID y mostrar los detalles del producto.
def buscar_producto():

    try:
        producto_a_buscar = input("¿Qué producto deseas consultar?: ")
        with open('inventario.txt', 'r') as archivo:
            inventario = archivo.readlines()
            archivo.seek(0)

        for item in inventario:
            if producto_a_buscar.lower() in item.lower():
                print(f"Producto encontrado: {item.strip()}")
                break
        else:
            print(f"Producto '{producto_a_buscar}' no encontrado en el inventario.")

    except FileNotFoundError:
        print("El archivo de inventario no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    print()
