import os, inputs as inp, menu, view, getproduct as get, searchproduct as search, modifyproduct as mod

def menu_supermercado(carrito):
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
            inp.automatizar_ingreso(carrito)
            os.system("pause")
        
        elif (opc == 2):
            print("* " * 24)
            view.mostrar_carrito(carrito)
            print("")
            print("* " * 24)
            view.mostrar_carrito_detallado(carrito)
            os.system("pause")

        elif (opc == 3):
            search.menu_busqueda(carrito)
            os.system("pause")

        elif (opc == 4):
            os.system("cls")
            print("*** MENU PARA MODIFICAR ATRIBUTOS ***")
            print("* " * 24)
            view.mostrar_carrito(carrito)
            print("")
            print("* " * 24)
            mod.modificar_producto(carrito)
            os.system("pause")
        
        elif (opc == 0):
            break;

        else:
            print("Por favor. Ingrese una opción valida.")
            