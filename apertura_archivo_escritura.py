#2.Apertura de archivo en modo escritura: Escribir datos de nuevos productos.
def escritura():
    print("--Sobrescribir inventario--")
    file = open("inventario.txt", "w")
    continuar = True
    while continuar == True:
        while True:
            nombre_articulo = input("Ingrese el nombre del producto: ").strip()
            if nombre_articulo:
                break
            else:
                print("El nombre no puede estar vacío.")
        while True:
            precio = input("Ingrese el precio del producto (USD): ").strip()
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
        file.write (f"{nombre_articulo}, {precio_articulo} USD, {cantidad_articulo} unidades, {talla_articulo}")
        file.write("\n")
        continuar= input("¿Desea agregar otro producto? (S/N): ")
        if continuar == "S" or continuar == "s":
            print()
            continuar = True
            print("Ingresando nuevo producto")
        elif continuar == "N" or continuar == "n":
            continuar = False
        else:
            print("Error: Ingrese una opción válida.")
    file.close()
    print("Inventario sobrescrito correctamente.")
    print()
escritura()