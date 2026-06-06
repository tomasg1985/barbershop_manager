# REGISTRO DE TURNO 

def registrar_turno(diccionario_clientes, nombre_cliente, servicios):
    
    """
    PROPOSITO:
    Vincula a un cliente con un servicio específico dentro de la base de datos, aquí buscamos crear una entrada directa donde el nombre sea el identificador único.
    
    PARAMETROS:
    diccionario_clientes (dict) -> Lugar de almacenaciento de informacion para persistencia durante su ejecución.
    nombre_cliente (str) -> Es la llave (key). Gracias a este dato, podemos encontrar, editar o borrar el turno después sin tener que buscar en toda la lista
    servicios (str) -> Etiqueta del servicio que el cliente quiere, la cual usamos para consultar el precio correcto en nuestro catálogo interno.
    
    FUNCIONAMIENTO:
    El Catálogo: La función tiene un "mini-diccionario" interno de precios. Esto la hace autónoma; no necesita que le digas cuánto cuesta cada cosa, ella ya lo sabe.
    La Validación: Antes de guardar nada, usa el operador in para chequear si el servicio solicitado existe. Si no existe, la función "se planta" y no guarda basura en los datos.
    Si todo está bien, guarda los datos directamente en el casillero del cliente: diccionario[nombre] = datos.
    
    RETORNO:
    Para que el menú principal (en tu app.py) pueda mostrar un mensaje verde de éxito o un error rojo, la función debe devolver un resultado.
    True: Si el servicio era válido y el turno se guardó.
    False: Si el servicio no fue reconocido.
    
    """
    
    precios_servicios = {
    "Corte": 3000,
    "Barba": 2000,
    "Color": 4500
}
    
    if servicios in precios_servicios:
        precio_final = precios_servicios[servicios]
    else:
        return
    
    nuevo_turno = {"cliente": nombre_cliente, "servicio": servicios, "precio": precio_final}
    
    diccionario_clientes[nombre_cliente] = {
        "servicio" : servicios,
        "precio" : precio_final
    }
    
    print(f"{nombre_cliente} Tu turno para {servicios} quedó registrado con éxito")
        
# ELIMINAR TURNO 
        
def eliminar_turno(clientes_registrados, nombre_cliente):
    
    """
    PROPOSITO:
    El objetivo principal de esta funcion es dar la baja a un cliente especifico de la base de datos. En lugar de buscar en una lista usamos un diccionario lo cual representa una gran ventaja haciendo mas eficiente la operacion que se realiza.
    
    PARAMETROS:
    diccionario_clientes (dict) -> El lugar donde están guardados todos los turnos del día.
    nombre_cliente (str) -> El identificador (llave) que queremos eliminar.
    
    FUNCIONAMIENTO:
    La Comprobación: Primero usamos el operador in para verificar si el cliente realmente tiene un turno. Esto evita que el programa tire un error si intentamos borrar a alguien que no existe.
    La Extracción: Si existe, usamos el método .pop() para quitar el registro completo de forma instantánea.
    
    RETORNO:
    True: Si el cliente existía y fue eliminado con éxito.
    False: Si el cliente no se encontró en el sistema.
    
    """
    
    if nombre_cliente in clientes_registrados:
        
        clientes_registrados.pop(nombre_cliente)
        
        print(f"El turno de {nombre_cliente} fue eliminado con éxito")
        
    else:
        print("ERROR: El cliente no tiene ningún turno registrado.")
        
# GENERAR REPORTE DEL DIA
        
def generar_reporte(lista_origen):
    
    """
    PROPOSITO:
    Mapeo de toda la actividad de la jornada para mostar un resumen detallado y el calculo total del dinero recaudado en caja.
    
    PARAMETROS:
    diccionario_clientes (dict) -> La fuente de datos con todos los turnos registrados.
    
    FUNCIONAMIENTO:
    Control de Vacío: Lo primero es chequear si hay datos. Si el diccionario está vacío, informa que no hubo actividad.
    El Recorrido: Usamos el método .items() para obtener simultáneamente el nombre del cliente y sus datos (servicio y precio).
    Acumulación: A medida que recorre cada turno, suma el valor de la llave "precio" a una variable total_caja.
    
    RETORNO:
    float / int: Devuelve el monto total recaudado para que pueda ser usado en otras funciones estadísticas si fuera necesario.
    
    """
    
    if lista_origen:
                
        total_caja = 0
        
        print("\n=== REPORTE DE TURNOS DE LA JORNADA ===")
        
        for cliente, datos in lista_origen.items():
            print(f"Cliente: {cliente.capitalize()} | Servicio: {datos['servicio']} | Precio: ${datos['precio']}")
            
            total_caja += datos["precio"]
            
        print(f"=======================================")
        print(f"Total recaudado en caja: ${total_caja}\n")
    else:
        print("No se registraron turnos en la jornada de hoy.")