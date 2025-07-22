while True:
    print("--MENÚ DE ANÁLISIS DE VENTAS--")
    print("1. Ingresar ventas ")
    print("2. Mostrar Ventas")
    print("3. Venta mas alta y venta mas baja")
    print("4. Promedio de ventas")
    print("5. Cuantos dias se superaron lo 1000")
    print("6. Buscar Venta especifica")
    print("7. Clasificar ventas")
    print("8. salir")
    opcion = int(input("Ingrese una opcion: "))
    listaVentas: []
    match opcion:
        case 1:
            cantidad = int(input("Cuantas ventas quiere realizar"))
            for i in cantidad:
                venta = int(input("Ingrese su lista de ventas"))
                if venta > 0:
                    listaVentas.append(cantidad)
                    print("Venta ingresada correctamente")
                else:
                    print("No se pudo ingresar su venta")
        case 2:
            if len(listaVentas) == 0:
                print("No hay ventas")
            else:
                for i in listaVentas:
                    print(f"Sus ventas son: {listaVentas}")
        case 3:
            print("multiplicanco")
        case 4:
            print("dividiendo")
        case 5:
            print("Salir")
            break
        case _:
            print("Opcion no valida")
