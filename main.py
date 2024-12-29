#import menu
import os
carrito = list()

def nombre_producto():
    os.system("cls")
    try:
        nombre = input("Ingrese el nombre del producto -->  ")
        if (len(nombre) <= 1):
            os.system("cls")
            print("Ingrese un nombre valido.")
            nombre = nombre_producto()
        return nombre
    except:
        os.system("cls")
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        nombre = nombre_producto()

def id_proveedor_producto():
    os.system("cls")
    try:
        id_proveedor = int(input("Ingrese el id del proveedor -->  "))

        if(id_proveedor <= 0):
            os.system("cls")
            print("Ingrese una ID valida")
            id_proveedor = id_proveedor_producto()

        return id_proveedor
    except:
        os.system("cls")
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        id_proveedor = id_proveedor_producto()

def nombre_proveedor_producto():
    os.system("cls")
    try:
        nombre_proveedor = input("Ingrese el nombre del proveedor -->  ")

        if (len(nombre_proveedor) <= 1):
            os.system("cls")
            print("Ingrese un nombre valido.")
            nombre_proveedor = nombre_proveedor_producto()
        return nombre_proveedor
    except:
        os.system("cls")
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        nombre_proveedor = nombre_proveedor_producto()

#! ----------------------------------------------- APARTADO INGRESAR PRODUCTO ------------------------------------

def ingresar_producto(nombre, id_proveedor, nombre_proveedor):

    producto: dict = {
        'Nombre': nombre,
        'Id_Proveedor': id_proveedor,
        'Nombre_Proveedor': nombre_proveedor
    }

    carrito.append(producto)

def automatizar_ingreso():
    os.system("cls")
    print("Ingresar productos")
    nombre = nombre_producto()
    os.system("cls")
    id_proveedor = id_proveedor_producto()
    os.system("cls")
    nombre_proveedor = nombre_proveedor_producto()
    os.system("cls")
    ingresar_producto(nombre, id_proveedor, nombre_proveedor)

def mostrar_carrito():
    for indice, producto in enumerate(carrito):
        print("")
        print("- " *10)
        print(f"ID: {indice + 1}")
        print(f"Nombre: {producto['Nombre']}")
        print("- " *10)


#! ----------------------------------------------- APARTADO MENU ------------------------------------
def menu_supermercado():
    while True:
        print("- " *24)
        print("Bienvenido al Supermercado")
        print("Elija una de las siguientes opciones")
        print("- " *24)
        
        print("")

        print("* " *24)
        print("[1] Ingresar producto al carrito.")
        print("[2] Mostrar productos ingresados")
        print("[3] Buscar productos")
        print("[4] Modificar carrito")
        print("[0] Salir.")
        print("* " *24)
        opc = int(input(""))

        if (opc == 1):
            automatizar_ingreso()
        
        elif (opc == 2):
            print("Mostrar productos")
            print("* " * 24)
            mostrar_carrito()
            print("")
            print("* " * 24)

        elif (opc == 3):
            print("Buscar producto")

        elif (opc == 4):
            print("Modificar carrito")
        
        elif (opc == 0):
            break;

        else:
            print("Por favor. Ingrese una opción valida.")
            

#! ------------------------------------------------------ MENU --------------------------------------------

menu_supermercado()
