import os, view
#! ----------------------------------------------- APARTADO OBTENER PRODUCTO ------------------------------------

def obtener_producto(carrito):
    try:
        indice = (int(input("Ingrese el ID del producto -->  ") ) - 1)
        if (indice < 0 or indice >= len(carrito)):
            os.system("cls")
            print("Ingrese una ID valida...")
            indice = view.mostrar_carrito_detallado()
        
        producto = carrito[indice]

        return producto
    
    except:
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return
        