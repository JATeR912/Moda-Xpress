#8.Eliminar un producto: Eliminar un producto del inventario.
def eliminar_producto():
    nombre_producto = input("¿Qué producto quieres eliminar?: ")
    
    if not nombre_producto:
        print("Debes ingresar el nombre de un producto. Operación cancelada.")
        return
    try:
        with open('inventario.txt', 'r') as archivo:
            inventario = archivo.readlines()

        with open('inventario.txt', 'w') as archivo:
            producto_eliminado = False
            
            for item in inventario:
                if nombre_producto.lower() not in item.lower():
                    archivo.write(item)
                else:
                    producto_eliminado = True

        if producto_eliminado:
            print(f"Producto '{nombre_producto}' eliminado del inventario.")
        else:
            print(f"Producto '{nombre_producto}' no encontrado en el inventario.")

    except FileNotFoundError:
        print("El archivo de inventario no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
print()