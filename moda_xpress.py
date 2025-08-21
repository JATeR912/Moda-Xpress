from datetime import datetime 
from apertura_archivo_lectura import mostrar_inventario #1.Apertura de archivo en modo lectura: Leer todo el inventario.
from apertura_archivo_escritura import escritura #2.Apertura de archivo en modo escritura: Escribir datos de nuevos productos.
from apertura_archivo_append import agregar_producto #3.Apertura de archivo en modo "append": Agregar productos sin eliminar los datos existentes.
from apertura_archivo_modificar import modificar_consultar #4.Apertura de archivo en modo lectura y escritura: Modificar y consultar productos existentes en el inventario.
from atributos_archivo_os import propiedades_inventario #5.Obtener atributos del archivo: Ver información sobre el archivo como el tamaño y la fecha de última modificación.
from leer_producto_especifico import buscar_producto #6.Leer un producto específico: Buscar por nombre o ID y mostrar los detalles del producto.
from modificar_nombre import modificar_nombre #7.Modificar el nombre de un producto: Cambiar el nombre de un artículo en el inventario.
from eliminar_producto import eliminar_producto #8.Eliminar un producto: Eliminar un producto del inventario.
#9.Cerrar archivos: Asegurarse de cerrar correctamente el archivo #Se reaiza de manera individual en cada función.
from backup import backup #10.Crear un backup del inventario: Guardar una copia de seguridad del inventario en un archivo separado.

menu= {1:"Consultar el inventario completo", 
        2:"Detalles de un producto",
        3:"Registrar nuevo producto",
        4:"Modificar los datos de un producto",
        5:"Modificar nombre del producto",
        6:"Eliminar productos del inventario",
        7:"Informacion propiedades del inventario",
        8:"Sobreescribir inventario",
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
     