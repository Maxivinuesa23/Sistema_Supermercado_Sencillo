import os


def nombre_producto():
    try:
        os.system("cls")
        nombre = input("Ingrese el nombre del producto -->  ")
        nombre = nombre.upper()
        if (len(nombre) <= 1):
            os.system("cls")
            print("Ingrese un nombre valido.")
            nombre = nombre_producto()
        return nombre
    except:
        os.system("cls")
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return

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
        return

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
        return
    

#! ----------------------------------------------- APARTADO INGRESAR PRODUCTO ------------------------------------

def ingresar_producto(nombre, id_proveedor, nombre_proveedor, carrito):
    try:
        producto: dict = {
            'Nombre': nombre,
            'Id_Proveedor': id_proveedor,
            'Nombre_Proveedor': nombre_proveedor
        }

        carrito.append(producto)
        print("🟢 EL PRODUCTO INGRESO CORRECTAMENTE AL CARRITO! 🟢")

    except:
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return

def automatizar_ingreso(carrito):
    try:
        os.system("cls")
        print("Ingresar productos")
        nombre = nombre_producto()
        os.system("cls")
        id_proveedor = id_proveedor_producto()
        os.system("cls")
        nombre_proveedor = nombre_proveedor_producto()
        os.system("cls")
        ingresar_producto(nombre, id_proveedor, nombre_proveedor, carrito)
    except:
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return