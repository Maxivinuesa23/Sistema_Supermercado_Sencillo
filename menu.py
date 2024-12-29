

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
            print("Ingresar productos")
        
        elif (opc == 2):
            print("Mostrar productos")

        elif (opc == 3):
            print("Buscar producto")

        elif (opc == 4):
            print("Modificar carrito")
        
        elif (opc == 0):
            break;

        else:
            print("Por favor. Ingrese una opción valida.")
            