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

    match opcion:
        case 1:
            print("Sumando")
        case 2:
            print("Restando")
        case 3:
            print("multiplicanco")
        case 4:
            print("dividiendo")
        case 5:
            print("Salir")
            break
        case _:
            print("Opcion no valida")
