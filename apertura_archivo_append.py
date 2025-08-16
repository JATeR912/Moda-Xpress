#3.Apertura de archivo en modo "append": Agregar productos sin eliminar los datos existentes.
def agregar_producto():
    print("--Registrar nuevo producto--")
    while True:
        nombre_articulo = input("Ingrese el nombre del producto: ").strip()
        if nombre_articulo:
            break
        else:
            print("El nombre no puede estar vacío.")
    while True:
        precio = input("Ingrese el precio del producto: ").strip()
        if not precio:
            print("El campo no puede estar vacío.")
            continue
        try:
            precio_articulo = int(precio)
            break  
        except ValueError:
            print("Error: El precio debe ser un número entero.")
    while True:
        cantidad = input("Ingrese la cantidad del producto: ").strip()
        if not cantidad:
            print("El campo no puede estar vacío.")
            continue
        try:
            cantidad_articulo = int(cantidad)
            break  
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")
    while True:
        talla_articulo = input("Ingrese la talla del producto: ").strip()
        if talla_articulo:
            break
        else:
            print("La talla no puede estar vacía.")
    try:
        with open("inventario.txt", "a") as file:
            file.write(f"{nombre_articulo}, {precio_articulo} USD, {cantidad_articulo} unidades, {talla_articulo}\n")
        print(f"Producto {nombre_articulo} agregado correctamente.")
    except Exception as e:
        print(f"Error: No se pudo agregar el producto. Detalles: {e}")
    print()
