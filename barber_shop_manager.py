while True:
    print("1. Registrar Turno - 2. Ver Reporte del Día - 3. Cerrar Sistema")
    opcion = input("Ingrese la opcion que desea consulta: ")
    
    opcion_valida = int(opcion)
    
    match opcion_valida:
        case 1:
            print("Funcionalidad de registro en desarrollo...")
        case 2:
            print("Funcionalidad de reporte en desarrollo...")
        case 3:
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción inválida. Intente de nuevo.")
            
    