from colorama import Back, Fore, Style, init
from logica_barberia import *
init(autoreset=True)

clientes_registrados = {}

while True:
    
    print(f"\n{Fore.CYAN}=== SISTEMA DE GESTIÓN BARBERÍA ===")
    print("1. Registrar Turno - 2. Ver Reporte - 3. Cancelar Turno - 4. Salir")
    
    opcion = input("Elija una opción: ").strip()
                
    match opcion:
        
        case "1":
            
            print(f"\n{Fore.YELLOW}--- Nuevo Registro ---")
            
            nombre = input("Nombre del cliente: ").strip().title()
            servicio = input("Servicio (Corte / Barba / Color): ").strip().title()
            
            if registrar_turno(clientes_registrados, nombre, servicio):
                print(f"{Fore.GREEN}¡Turno de {nombre} para {servicio} guardado con éxito!")
            else:
                print(f"{Fore.RED}ERROR: El servicio '{servicio}' no es válido.")
            
        case "2":
            
            generar_reporte(clientes_registrados)
            
        case "3":
            
            cliente_baja = input("Nombre del cliente para cancelar: ").strip().title()
            
            if eliminar_turno(clientes_registrados, cliente_baja):
                print(f"{Fore.GREEN}El turno fue eliminado correctamente.")
            else:
                print(f"{Fore.RED}ERROR: No se encontró un turno para {cliente_baja}.")
        
        case "4":
            
            print(f"{Fore.MAGENTA}Cerrando sistema... ¡Buen trabajo hoy!")
            break
        
        case _:
            
            print(f"{Fore.RED}Opción inválida. Intente de nuevo.")