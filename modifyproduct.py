import inputs as inp, getproduct as get
#! ----------------------------------------------- APARTADO MODIFICAR PRODUCTO ------------------------------------

def modificar_producto(carrito): 
    try:
        if not carrito:
            print("No hay productos ingresados")
        else:
            producto = get.obtener_producto(carrito)

            print("¿Que atributo desea modificar?")
            print("[1] Nombre del producto")
            print("[2] Nombre del proveedor")
            print("[3] ID del proveedor")
            print("[0] Salir.")
            opcion = int(input("-->  "))

            if (opcion == 1):
                producto['Nombre'] = inp.nombre_producto()
                print("Nombre modificado exitosamente! 🟢")
            elif (opcion == 2):
                producto['Nombre_Proveedor'] = inp.nombre_proveedor_producto()
                print("Nombre del proveedor modificado exitosamente! 🟢")
            elif (opcion == 3):
                producto['Id_Proveedor'] = inp.id_proveedor_producto()
                print("ID del proveedor modificado exitosamente! 🟢")
            elif (opcion == 0):
                return
            else:
                print("Elija una opción valida.")
                modificar_producto(carrito)
            return

    except:
        print("Ha ocurrido un error pero no te preocupes. Vuelve a intentarlo!")
        return
