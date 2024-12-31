import os, view

#! ----------------------------------------------- APARTADO BUSCAR PRODUCTO POR NOMBRE ------------------------------------
def buscar_producto_nombre(carrito):
    
    try:
        if not carrito:
            print("No hay productos ingresados")
        else:
            nombre_producto = input("Ingrese el nombre del producto a buscar -->  ")
            nombre_producto = nombre_producto.upper()

            os.system("cls")
            for indice, producto in enumerate(carrito):
                if (nombre_producto in producto['Nombre']):
                    control = 1
                    print("")
                    print("- " *10)
                    print(f"ID: {indice + 1}")
                    print(f"Nombre: {producto['Nombre']}")
                    print("- " *10)
                else:
                    return
            
            return control

    except:
        print("Ha ocurrido un error o el producto no se encontro pero no te preocupes. Vuelve a intentarlo!")
        return

def buscar_producto_id_proveedor(carrito):
    try:
        if not carrito:
            print("No hay productos ingresados")
            return
        else:
            id_proveedor = int(input("Ingrese el ID del proveedor -->  "))

            os.system("cls")
            print(f"Productos del proveedor con ID: {id_proveedor}")
            for indice, producto in enumerate(carrito):
                if (id_proveedor == producto['Id_Proveedor']):
                    control = 1
                    print("")
                    print("- " *10)
                    print(f"ID: {indice + 1}")
                    print(f"Nombre: {producto['Nombre']}")
                    print("- " *10)
                else:
                    return

            return control
    except:
        print("Ha ocurrido un error o el producto no se encontro pero no te preocupes. Vuelve a intentarlo!")
        return

def buscar_producto_proveedor(carrito):
    try:
        if not carrito:
            print("No hay productos ingresados")
            return
        else:
            nombre_proveedor = input("Ingrese el nombre del proveedor -->  ")

            os.system("cls")
            for indice, producto in enumerate(carrito):
                if (nombre_proveedor in producto['Nombre_Proveedor']):
                    control = 1
                    print("")
                    print("- " *10)
                    print(f"ID: {indice + 1}")
                    print(f"Nombre: {producto['Nombre']}")
                    print(f"Proveedor: {producto['Nombre_Proveedor']}")
                    print("- " *10)
                else:
                    return 

            return control
    except:
        print("Ha ocurrido un error o el producto no se encontro pero no te preocupes. Vuelve a intentarlo!")
        return

def menu_busqueda(carrito):
    os.system("cls")
    print("Elija una opción por la que desea buscar")
    print("[1] Nombre del producto")
    print("[2] Nombre del proveedor")
    print("[3] ID del proveedor")
    print("[0] Salir.")
    opcion = int(input(" -->  "))

    if (opcion == 1):
        control = buscar_producto_nombre(carrito)

        if (control == 1):
            view.mostrar_carrito_detallado(carrito)
        else:
            print("No se pudo encontrar el producto")
    elif (opcion == 2):
        control = buscar_producto_proveedor(carrito)

        if (control == 1):
            view.mostrar_carrito_detallado(carrito)
        else:
            print("No se pudo encontrar el producto")

    elif (opcion == 3):
        control = buscar_producto_id_proveedor(carrito)

        if (control == 1):
            view.mostrar_carrito_detallado(carrito)
        else:
            print("No se pudo encontrar el producto")

    elif (opcion == 0):
        return
    else:
        print("Elija una opción valida.")
