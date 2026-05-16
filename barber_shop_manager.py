corte = 3000
barba = 2000
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
            
            if servicios == "Corte":
                
                print(f"El precio por corte es de: {corte}")
                precio_final = corte
                
            elif servicios == "Barba":
                
                print(f"El precio por barba es de: {barba}")
                precio_final = barba
                
            else:
                print(f"ERROR: Servicio no reconocido. Turno cancelado.")
                continue
            
            
            clientes_registrados.append(nombre_cliente)
            servicios_solicitados.append(servicios)
            caja_dia.append(precio_final)
            
            print(f"{nombre_cliente} Tu turno para {servicios} quedó registrado con éxito")
            
        case "2":
            
            if clientes_registrados:
                print(f"\nClientes de hoy: {clientes_registrados}")
                print(f"Servicios realizados: {servicios_solicitados}")
                print(f"Total recaudado en caja: ${sum(caja_dia)}")
            else:
                print("No se registraron turnos en la jornada de hoy.")
                
        case "3":
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción inválida. Intente de nuevo.")
            
    