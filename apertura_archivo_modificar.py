#4.Apertura de archivo en modo lectura y escritura: Modificar y consultar productos existentes en el inventario.
def modificar_consultar():
    nombre_producto = input("¿Qué producto quieres buscar?: ")
    
    if not nombre_producto.strip():
        print("Debes ingresar el nombre de un producto.")
        return

    try:

        with open('inventario.txt', 'r+', encoding='utf-8') as archivo:
            inventario = archivo.readlines()
            producto_encontrado = False

            for i, item in enumerate(inventario):
                if nombre_producto.lower() in item.lower():
                    print(f"Producto encontrado: {item.strip()}")
                    producto_encontrado = True

                    accion = input("¿Qué deseas hacer? 1=Solo consultar, 2=Modificar: ")

                    if accion == "1":
                        print("Consulta completada.")
                        return
                    elif accion == "2":
                        separar_partes = item.strip().split(", ")

                        print("¿Qué deseas modificar?")
                        print("1=Nombre, 2=Precio, 3=Cantidad, 4=Talla, 5=Todo")
                        opcion = input("Opción: ")

                        nuevo_nombre = separar_partes[0]
                        nuevo_precio = separar_partes[1]
                        nueva_cantidad = separar_partes[2]
                        nueva_talla = separar_partes[3]

                        if opcion == "1":
                            nuevo_nombre = input(f"Nuevo nombre ({separar_partes[0]}): ") or separar_partes[0]
                        elif opcion == "2":
                            nuevo_precio = input(f"Nuevo precio ({separar_partes[1]}): ") or separar_partes[1]
                        elif opcion == "3":
                            nueva_cantidad = input(f"Nueva cantidad ({separar_partes[2]}): ") or separar_partes[2]
                        elif opcion == "4":
                            nueva_talla = input(f"Nueva talla ({separar_partes[3]}): ") or separar_partes[3]
                        elif opcion == "5":
                            nuevo_nombre = input(f"Nombre ({separar_partes[0]}): ") or separar_partes[0]
                            nuevo_precio = input(f"Precio ({separar_partes[1]}): ") or separar_partes[1]
                            nueva_cantidad = input(f"Cantidad ({separar_partes[2]}): ") or separar_partes[2]
                            nueva_talla = input(f"Talla ({separar_partes[3]}): ") or separar_partes[3]
                        else:
                            print("Opción inválida.")
                            return

                        separar_partes = [nuevo_nombre, nuevo_precio, nueva_cantidad, nueva_talla]
                        inventario[i] = ", ".join(separar_partes) + "\n"
                        archivo.seek(0) # hay que volver al inicio y truncar el archivo
                        archivo.truncate()
                        archivo.writelines(inventario)

                        print(f"Producto actualizado: {', '.join(separar_partes)}")
                        print("¡Producto modificado exitosamente!")
                        return
                    else:
                        print("Opción inválida.")
                        return

            if not producto_encontrado:
                    print(f"El producto '{nombre_producto}' no se encontró en el inventario.")

    except FileNotFoundError:
        print("El archivo de inventario no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

print()
    