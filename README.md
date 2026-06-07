# 🔐 Gestor de Contraseñas Local

Un sistema de gestión de credenciales estructurado desarrollado en **Python** como parte del programa de formación en **Talento Tech**. Este proyecto representa una evolución técnica significativa, migrando de estructuras de datos lineales hacia una arquitectura optimizada con diccionarios y una separación estricta de responsabilidades.

---

### 🚀 Características Técnicas

*   **Arquitectura Modular:** Separación estricta de responsabilidades (SoC) entre la interfaz de usuario y la lógica de negocio profunda.
*   **Eficiencia Alogrítmica $O(1)$:** Uso estratégico de diccionarios para garantizar búsquedas, ediciones y eliminaciones instantáneas mediante claves únicas (cuentas), optimizando drásticamente el rendimiento frente a estructuras basadas en listas.
*   **Validación Estricta:** Implementación de controles de flujo defensivos para mitigar campos vacíos y asegurar la integridad del almacenamiento local.
*   **Experiencia de Usuario (UX):** Interfaz interactiva por línea de comandos potenciada con la librería **Colorama**, proporcionando un sistema de alertas visuales intuitivo (Éxitos en verde, Errores en rojo y Advertencias en amarillo).
*   **Documentación Rigurosa:** Funciones *core* completamente documentadas mediante **Docstrings** que detallan de forma explícita el propósito, tipos de parámetros y esquemas de retorno.

---

### 🛠️ Stack Tecnológico

*   **Lenguaje:** Python 3.x
*   **Librerías:** [Colorama](https://pypi.org) (Formateo de color y control de salida en consola)

---

### 📂 Estructura y Arquitectura de Archivos



| Archivo | Rol en la Arquitectura | Descripción Técnica |
| :--- | :--- | :--- |
| `app.py` | **Capa de Presentación** | Punto de entrada de la aplicación. Orquesta el menú interactivo mediante la instrucción nativa `match` y procesa la entrada del usuario. |
| `logica_gestor.py` | **Capa de Negocio** | Motor lógico autónomo. Encapsula las funciones *core* de administración: `nueva_contrasena`, `ver_contrasena`, `eliminar_contrasena` y `editar_contrasena`. |

---

### ⚙️ Instalación y Ejecución

Sigue estos pasos para clonar, configurar y ejecutar la aplicación de forma local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   cd gestor_de_contrasenas
   ```

2. **Instalar las dependencias necesarias:**
   ```bash
   pip install colorama
   ```

3. **Iniciar la interfaz:**
   ```bash
   python app.py
   ```

---

### 📄 Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo de origen para más información.
