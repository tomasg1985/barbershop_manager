clientes_registrados = []
servicios_solicitados = []
caja_dia = []

while True:
    print("1. Registrar Turno - 2. Ver Reporte del Día - 3. Cerrar Sistema")
    opcion = input("Ingrese la opcion que desea consulta: ")
    
    match opcion:
        case "1":
            
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip().title()
            servicios = input("Seleccione el servicio que desea (Elija Corte o Barba): ").strip().title()
            
            clientes_registrados.append(nombre_cliente)
            servicios_solicitados.append(servicios)
            
            print(f"{nombre_cliente} Tu turno para {servicios} quedó registrado con éxito")
            
        case "2":
            print("Funcionalidad de reporte en desarrollo...")
        case "3":
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción inválida. Intente de nuevo.")
            
    