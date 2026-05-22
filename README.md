# 💈 BarberShop Manager - Sistema de Gestión de Turnos y Caja

Software interactivo de consola desarrollado en Python para la administración centralizada de turnos, control de servicios y auditoría de caja diaria para una barbería. Aplica un enfoque corporativo mediante programación defensiva, control estricto de flujo y sincronización indexada de estructuras lineales.

Este proyecto forma parte de un portafolio técnico que demuestra el dominio en la persistencia temporal en memoria, manipulación avanzada de colecciones y mitigación de errores de lógica o ejecución en entornos interactivos.

---

## 🚀 Funcionalidades Implementadas

* **Módulo de Altas (Registrar Turno)**: Captura y sanitización de datos de clientes y servicios mediante métodos de cadenas (`.strip().title()`). Implementa un sistema de tarifas fijas automatizado según la opción seleccionada.
* **Control de Excepciones Lógicas (Filtros de Flujo)**: Desvío preventivo mediante la sentencia `continue` que aborta el registro de datos si el usuario ingresa un servicio no contemplado en el catálogo comercial, evitando registros fantasmas o desincronizados.
* **Módulo de Bajas (Cancelar Turno)**: Implementación de lógica de eliminación indexada. El sistema busca la existencia del cliente mediante el operador `in`, localiza su ubicación en memoria con `.index()` y remueve en simultáneo los datos de las tres listas (`clientes`, `servicios` y `caja`) utilizando `.pop(posicion)`.
* **Módulo de Auditoría (Reporte de Jornada)**: Sistema de control que valida la existencia de movimientos comerciales antes de generar reportes. Utiliza funciones de agregación (`sum()`) para desglosar la recaudación neta, el historial de clientes y los servicios prestados.

---

## 🛠️ Conceptos Técnicos Consolidados (Guía 7)

* **Estructuras de Datos Lineales**: Inicialización, lectura, mutación y vaciado controlado de listas dinámicas (`[]`).
* **Sincronización por Índices**: Coherencia relacional entre múltiples estructuras de datos independientes conectadas mediante su número de posición física en memoria.
* **Flujos de Control Interactivos**: Bucles infinitos eficientes (`while True`), enrutamiento limpio mediante estructuras múltiples (`match/case`) y cortes de ejecución controlados (`break`).

---

## 📋 Arquitectura de la Interfaz (Consola)

```text
=== CONTROL DE OPERACIONES ===
1. Registrar Turno - 2. Ver Reporte del Día - 3. Cancelar Turno - 4. Cerrar Sistema

Ingrese la opcion que desea consultar: 1
Ingrese el nombre del cliente: tomas
Seleccione el servicio que desea (Elija Corte o Barba): corte
El precio por corte es de: 3000
Tomas Tu turno para Corte quedó registrado con éxito

Ingrese la opcion que desea consultar: 2
Clientes de hoy: ['Tomas']
Servicios realizados: ['Corte']
Total recaudado en caja: $3000

Ingrese la opcion que desea consultar: 3
Indique el nombre del cliente para dar de baja: tomas
Cliente encontrado
El turno de Tomas fue eliminado con éxito
```

---

## 🎓 Trayecto Formativo
Proyecto de nivelación y consolidación de base desarrollado de forma incremental como parte del trayecto formativo en **Talento Tech (Guías 1-7)**. Demuestra la capacidad de estructurar sistemas interactivos comerciales robustos mediante algoritmos de búsqueda y extracción sobre colecciones indexadas.
