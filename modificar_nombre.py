#7.Modificar el nombre de un producto: Cambiar el nombre de un artículo en el inventario.
def modificar_nombre():
    nombre_producto = input("¿Qué producto quieres renombrar?: ")

    try:
        with open('inventario.txt', 'r') as archivo:
            inventario = archivo.readlines()

        producto_encontrado = False

        with open('inventario.txt', 'w') as archivo:
            for item in inventario:
                if nombre_producto.lower() in item.lower():
                    producto_encontrado = True
                    print(f"Producto encontrado: {item.strip()}")

                    nuevo_nombre = input(f"Nuevo nombre para el producto ({item.strip().split(', ')[0]}): ")
                    if nuevo_nombre:
                        item = item.replace(item.strip().split(', ')[0], nuevo_nombre)

                    archivo.write(item)
                    print(f"Producto actualizado: {item.strip()}")
                else:
                    archivo.write(item)

        if not producto_encontrado:
            print(f"Producto '{nombre_producto}' no encontrado en el inventario.")

    except FileNotFoundError:
        print("El archivo de inventario no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    print()
