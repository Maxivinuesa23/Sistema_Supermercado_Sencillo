import os, getproduct as get

#! ----------------------------------------------- APARTADO VER CARRITO ------------------------------------
def mostrar_carrito(carrito):
    try:
        os.system("cls")
        if not carrito:
            print("No hay productos para mostrar")
        else:
            for indice, producto in enumerate(carrito):
                print("")
                print("- " *10)
                print(f"ID: {indice + 1}")
                print(f"Nombre: {producto['Nombre']}")
                print("- " *10)
    except:
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return


def mostrar_carrito_detallado(carrito):
    try:
        condicional = int(input("¿Desea ver detalles? \n[1] SI\n[2] NO\n -->  "))
        if (condicional == 1):
            producto = get.obtener_producto(carrito)
            print("")
            print("- " *10)
            print(f"Nombre: {producto['Nombre']}")
            print(f"ID Proveedor: {producto['Id_Proveedor']}")
            print(f"Nombre Proveedor: {producto['Nombre_Proveedor']}")
            print("- " *10)
        elif (condicional == 2):
            return
        else:
            print("Ingrese una opción valida.")
            os.system("pause")
            mostrar_carrito_detallado(carrito)
        
    except:
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return
    