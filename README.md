# 💈 Sistema de Gestión Barbería - TalentoLab

Este proyecto es una aplicación de consola desarrollada en **Python** diseñada para gestionar los turnos y la contabilidad diaria de una barbería. Representa una evolución técnica desde un prototipo basado en listas hacia una arquitectura profesional optimizada con **diccionarios**, **modularización** y **validación robusta**.

## 🚀 Características Principales

*   **Arquitectura Modular**: Separación de responsabilidades entre la interfaz (`app_barberia.py`) y el motor lógico (`logica_barberia.py`), facilitando el mantenimiento y la escalabilidad.
*   **Eficiencia O(1)**: Implementación de diccionarios para el almacenamiento de clientes, permitiendo búsquedas, bajas y registros instantáneos mediante claves únicas.
*   **Gestión de Flujo Senior**: Uso de retornos booleanos en funciones lógicas para controlar dinámicamente los mensajes de éxito o error en la interfaz de usuario.
*   **Sanitización de Datos**: Limpieza automática de entradas mediante métodos como `.strip()` y `.title()`, asegurando la integridad de la base de datos.
*   **Interfaz con Colorama**: Experiencia de usuario (UX) mejorada con feedback visual coloreado para distinguir alertas, éxitos y menús.
*   **Documentación Técnica**: Todas las funciones incluyen **Docstrings** profesionales que detallan su propósito, parámetros y valores de retorno.

## 🛠️ Tecnologías Utilizadas

*   **Python 3.x**
*   **Colorama**: Librería para el estilizado de la terminal.

## 📂 Estructura del Proyecto

1.  **`app_barberia.py`**: Punto de entrada del sistema. Gestiona el menú interactivo mediante `match-case` y la interacción directa con el usuario.
2.  **`logica_barberia.py`**: Núcleo lógico que procesa los registros, cálculos de caja y eliminaciones, manteniendo la autonomía del sistema.

## 🔧 Instalación y Uso

1.  Clona este repositorio.
2.  Instala Colorama:
    ```bash
    pip install colorama
3.  Ejecuta la aplicación:
    ```bash
    python app_barberia.py
