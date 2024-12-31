
#! CODIGO SIN MODULOS

#import menu
import os, inputs, menu
carrito = list()

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

def ingresar_producto(nombre, id_proveedor, nombre_proveedor):
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

def automatizar_ingreso():
    try:
        os.system("cls")
        print("Ingresar productos")
        nombre = nombre_producto()
        os.system("cls")
        id_proveedor = id_proveedor_producto()
        os.system("cls")
        nombre_proveedor = nombre_proveedor_producto()
        os.system("cls")
        ingresar_producto(nombre, id_proveedor, nombre_proveedor)
    except:
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return


#! ----------------------------------------------- APARTADO VER CARRITO ------------------------------------
def mostrar_carrito():
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


def mostrar_carrito_detallado():
    try:
        condicional = int(input("¿Desea ver detalles? \n[1] SI\n[2] NO\n -->  "))
        if (condicional == 1):
            producto = obtener_producto()
            print("")
            print("- " *10)
            print(f"Nombre: {producto['Nombre']}")
            print(f"ID Proveedor: {producto['Id_Proveedor']}")
            print(f"Nombre Proveedor: {producto['Nombre_Proveedor']}")
            print("- " *10)
        else:
            return
        
    except:
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return
    
#! ----------------------------------------------- APARTADO OBTENER PRODUCTO ------------------------------------

def obtener_producto():
    try:
        indice = (int(input("Ingrese el ID del producto -->  ") ) - 1)
        if (indice < 0 or indice >= len(carrito)):
            os.system("cls")
            print("Ingrese una ID valida...")
            indice = mostrar_carrito_detallado()
        
        producto = carrito[indice]

        return producto
    
    except:
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return
        
#! ----------------------------------------------- APARTADO BUSCAR PRODUCTO POR NOMBRE ------------------------------------
def buscar_producto_nombre():
    
    try:
        if not carrito:
            print("No hay productos ingresados")
        else:
            nombre_producto = input("Ingrese el nombre del producto a buscar -->  ")
            nombre_producto = nombre_producto.upper()

            os.system("cls")
            for indice, producto in enumerate(carrito):
                if (nombre_producto in producto['Nombre']):
                    control = True
                    print("")
                    print("- " *10)
                    print(f"ID: {indice + 1}")
                    print(f"Nombre: {producto['Nombre']}")
                    print("- " *10)
            
            if control == True:
                mostrar_carrito_detallado()

            return
    
    except:
        print("Ha ocurrido un error o el producto no se encontro pero no te preocupes. Vuelve a intentarlo!")
        return

def buscar_producto_id_proveedor():
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
                    control = True
                    print("")
                    print("- " *10)
                    print(f"ID: {indice + 1}")
                    print(f"Nombre: {producto['Nombre']}")
                    print("- " *10)

            if control:
                mostrar_carrito_detallado()

            return
    except:
        print("Ha ocurrido un error o el producto no se encontro pero no te preocupes. Vuelve a intentarlo!")
        return

def buscar_producto_proveedor():
    try:
        if not carrito:
            print("No hay productos ingresados")
            return
        else:
            nombre_proveedor = input("Ingrese el nombre del proveedor -->  ")

            os.system("cls")
            for indice, producto in enumerate(carrito):
                if (nombre_proveedor in producto['Nombre_Proveedor']):
                    control = True
                    print("")
                    print("- " *10)
                    print(f"ID: {indice + 1}")
                    print(f"Nombre: {producto['Nombre']}")
                    print(f"Proveedor: {producto['Nombre_Proveedor']}")
                    print("- " *10)

            if control:
                mostrar_carrito_detallado()

            return
    except:
        print("Ha ocurrido un error o el producto no se encontro pero no te preocupes. Vuelve a intentarlo!")
        return

def menu_busqueda():
    os.system("cls")
    print("Elija una opción por la que desea buscar")
    print("[1] Nombre del producto")
    print("[2] Nombre del proveedor")
    print("[3] ID del proveedor")
    print("[0] Salir.")
    opcion = int(input(" -->  "))

    if (opcion == 1):
        buscar_producto_nombre()
    elif (opcion == 2):
        buscar_producto_proveedor()
    elif (opcion == 3):
        buscar_producto_id_proveedor()
    elif (opcion == 0):
        return
    else:
        print("Elija una opción valida.")

#! ----------------------------------------------- APARTADO MODIFICAR PRODUCTO ------------------------------------

def modificar_producto(): 
    try:
        if not carrito:
            print("No hay productos ingresados")
        else:
            producto = obtener_producto()

            print("¿Que atributo desea modificar?")
            print("[1] Nombre del producto")
            print("[2] Nombre del proveedor")
            print("[3] ID del proveedor")
            print("[0] Salir.")
            opcion = int(input("-->  "))

            if (opcion == 1):
                producto['Nombre'] = nombre_producto()
                print("Nombre modificado exitosamente! 🟢")
            elif (opcion == 2):
                producto['Nombre_Proveedor'] = nombre_proveedor_producto()
                print("Nombre del proveedor modificado exitosamente! 🟢")
            elif (opcion == 3):
                producto['Id_Proveedor'] = id_proveedor_producto()
                print("ID del proveedor modificado exitosamente! 🟢")
            elif (opcion == 0):
                return
            else:
                print("Elija una opción valida.")
                modificar_producto()
            return

    except:
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return


#! ----------------------------------------------- APARTADO MENU ------------------------------------
def menu_supermercado():
    while True:
        os.system("cls")
        print("⭐ Bienvenido al Supermercado ⭐")
        print("Elija una de las siguientes opciones")

        print("* " *24)
        print("[1] Ingresar producto al carrito. 🛒")
        print("[2] Mostrar productos ingresados 👁️‍🗨️")
        print("[3] Buscar productos 🔎")
        print("[4] Modificar carrito 🔃")
        print("[0] Salir. 👋")
        print("* " *24)
        opc = int(input(""))

        if (opc == 1):
            automatizar_ingreso()
            os.system("pause")
        
        elif (opc == 2):
            print("* " * 24)
            mostrar_carrito()
            print("")
            print("* " * 24)
            mostrar_carrito_detallado()
            os.system("pause")

        elif (opc == 3):
            menu_busqueda()
            os.system("pause")

        elif (opc == 4):
            os.system("cls")
            print("*** MENU PARA MODIFICAR ATRIBUTOS ***")
            print("* " * 24)
            mostrar_carrito()
            print("")
            print("* " * 24)
            modificar_producto()
            os.system("pause")
        
        elif (opc == 0):
            break;

        else:
            print("Por favor. Ingrese una opción valida.")
            

#! ------------------------------------------------------ MENU --------------------------------------------

menu_supermercado()
