corte = 3000
barba = 2000
clientes_registrados = []
servicios_solicitados = []
caja_dia = []

while True:
    print("1. Registrar Turno - 2. Ver Reporte del Día - 3. Cancelar Turno - 4. Cerrar Sistema")
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
            
            nuevo_turno = {
                "cliente" : nombre_cliente,
                "servicio" : servicios,
                "precio" : precio_final
            }
            
            clientes_registrados.append(nuevo_turno)
            
            print(f"{nombre_cliente} Tu turno para {servicios} quedó registrado con éxito")
            
        case "2":
            
            if clientes_registrados:
                
                total_caja = 0
                
                print("\n=== REPORTE DE TURNOS DE LA JORNADA ===")
                
                for turno in clientes_registrados:
                    print(f"Cliente: {turno['cliente']} | Servicio: {turno['servicio']} | Precio: ${turno['precio']}")
                    
                    total_caja += turno["precio"]
                    
                print(f"=======================================")
                print(f"Total recaudado en caja: ${total_caja}\n")
            else:
                print("No se registraron turnos en la jornada de hoy.")
                
        case "3":
            
            cliente_baja = input("Indique el nombre del cliente para dar de baja: ").strip().title()
            
            posicion_encontrada = -1
            
            for i in range(len(clientes_registrados)):
                if clientes_registrados[i]["cliente"] == cliente_baja:
                    posicion_encontrada = i
                    break
                
            if posicion_encontrada != -1:
                print("Cliente encontrado")
                
                clientes_registrados.pop(posicion_encontrada)
                
                print(f"El turno de {cliente_baja} fue eliminado con éxito")
                
            else:
                print("ERROR: El cliente no tiene ningún turno registrado.")
            
            
        case "4":
            
            print("Saliendo del sistema...")
            break
        
        case _:
            
            print("Opción inválida. Intente de nuevo.")
            
    