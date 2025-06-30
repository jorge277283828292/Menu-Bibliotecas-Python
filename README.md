# 📚 Menú de Bibliotecas Python

Este proyecto es un menú interactivo hecho en Python que permite al usuario explorar ejemplos prácticos de **10 bibliotecas estándar** de Python. Cada opción del menú ejecuta un pequeño programa relacionado con una de estas bibliotecas.

---

## 🚀 ¿Qué hace este proyecto?

🔹 Muestra un menú de opciones donde el usuario puede seleccionar una biblioteca.  
🔹 Ejecuta un programa práctico relacionado con la biblioteca seleccionada.  
🔹 Espera 3 segundos después de la ejecución antes de volver al menú.  
🔹 Está organizado por carpetas, cada una dedicada a una biblioteca.

---

## 📁 Estructura del Proyecto

```bash
Menu Bibliotecas Python/
├── main.py                # Archivo principal que muestra el menú
├── opcions/              # Módulo con funciones de información del menú
│   └── informacion.py
├── prog_calendar/        # Programa con ejemplo usando 'calendar'
│   └── main.py
├── prog_datetime/        # Programa para calcular edad con 'datetime'
│   └── edades.py
├── prog_os/              # Funciones básicas del sistema con 'os'
├── prog_json/            # Lectura/escritura de JSON
├── prog_math/            # Cálculos matemáticos con 'math'
├── prog_secrets/         # Generación de datos seguros
├── prog_random/          # Juego de adivinar número
│   └── adivinar.py
├── prog_re/              # Validación de cadenas con 're'
├── prog_statistics/      # Estadísticas básicas con 'statistics'
├── prog_time/            # Temporizador y reloj con 'time'
