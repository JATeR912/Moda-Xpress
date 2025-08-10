from moda_xpress import mostrar_inventario

menu= {1:"Consultar el inventario completo", 
        2:"Detalles de un producto",
        3:"Registrar nuevo producto",
        4:"Modificar los datos de un producto",
        5:"Modificar nombre del producto",
        6:"Eliminar productos del inventario",
        7:"Informacion propiedades del inventario",
        8:"Crear nuevo inventario",
        9:"Crear backup del inventario",
        0:"Salir"}

print("Menu de Opciones")
print(menu)
seleccion = " "
while seleccion != 0:
    print("Menu de Opciones")
    for option in menu:
        print (f"{option}:{menu[option]}")
    seleccion = input("Ingrese el numero de la opcion que desea realizar: ") 
    if seleccion == "1":
        mostrar_inventario()

    elif seleccion == "2":
        buscar_producto()

    elif seleccion == "3":
        agregar_producto()
        
    elif seleccion == "4":
        modificar_consultar()
       
    elif seleccion == "5":
        modificar_nombre()

    elif seleccion == "6":
        eliminar_producto()

    elif seleccion == "7":
        propiedades_inventario()

    elif seleccion == "8":
        escritura()

    elif seleccion == "9":
        backup()

    elif seleccion == "0":
        break
    else:
        print("Opcion no valida")
     