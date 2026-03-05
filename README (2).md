# 📘 Taller 2: Python — Estructuras de Control y Funciones

Este repositorio contiene un **taller práctico** de Python enfocado en:
- Manejo de variables y entrada de datos
- Condicionales
- Ciclos `for` y `while`
- Listas y diccionarios
- Creación y uso de funciones citeturn4search1  

---

## 🎯 Objetivo
Fortalecer la lógica de programación mediante la implementación de **ejercicios progresivos** organizados por secciones temáticas. citeturn4search1  

---

## ✅ Requisitos
- Python 3.x (recomendado)
- Editor de código (VS Code u otro)

---

## ▶️ ¿Cómo ejecutar?
Si tu repositorio incluye un archivo `index.py` como punto de entrada, puedes ejecutarlo así: citeturn4search1  

```bash
python index.py
```

En macOS/Linux, si usas `python3`:

```bash
python3 index.py
```

---

## 🗂️ Encarpetado (estructura del proyecto)

```text
taller2_Estructuras de control y Funciones/
├─ README.md                    # Se puede realizar con alguna IA
├─ requirements.txt             # Enunciados de los ejercicios
├─ taller/                      # Paquete principal (código fuente)
│  ├─ seccion1/                 # MANEJO DE VARIABLES Y ENTRADA DE DATOS
│  │  ├─ algoritmo_1.1.py
│  │  ├─ algoritmo_1.2.py
│  │  ├─ algoritmo_1.3.py
│  │  ├─ algoritmo_1.4.py
│  │  └─ algoritmo_1.5.py
│  ├─ seccion2/                 # IMPLEMENTACIÓN DE CONDICIONALES
│  │  ├─ algoritmo_2.1.py
│  │  ├─ algoritmo_2.2.py
│  │  ├─ algoritmo_2.3.py
│  │  ├─ algoritmo_2.4.py
│  │  └─ algoritmo_2.5.py
│  ├─ seccion3/                 # USO DE CICLOS FOR Y WHILE
│  │  ├─ algoritmo_3.1.py
│  │  ├─ algoritmo_3.2.py
│  │  ├─ algoritmo_3.3.py
│  │  ├─ algoritmo_3.4.py
│  │  └─ algoritmo_3.5.py
│  ├─ seccion4/                 # GESTIÓN DE LISTAS Y DICCIONARIOS
│  │  ├─ algoritmo_4.1.py
│  │  ├─ algoritmo_4.2.py
│  │  ├─ algoritmo_4.3.py
│  │  ├─ algoritmo_4.4.py
│  │  └─ algoritmo_4.5.py
│  └─ seccion5/                 # CREACIÓN Y USO DE FUNCIONES
│     ├─ algoritmo_5.1.py
│     ├─ algoritmo_5.2.py
│     ├─ algoritmo_5.3.py
│     ├─ algoritmo_5.4.py
│     └─ algoritmo_5.5.py
└─ seccion6/                    # MINI-TALLER INTEGRADOR
   └─ biblioteca.py
```

> 💡 Recomendación: en cada archivo `algoritmo_X.Y.py` define una función `run()` (o `main()`) para ejecutar el ejercicio desde consola.

---

## 📌 Enunciados del Taller

### ✅ SECCIÓN 1: Manejo de Variables y Entrada de Datos

**Ejercicio 1.1 – Registro de usuario**  
Solicitar: nombre, edad y ciudad. Mostrar:  
> “Hola [nombre], tienes [edad] años y vives en [ciudad].”  
Validar que la edad sea un número positivo. citeturn4search1  

**Ejercicio 1.2 – Calculadora básica**  
Pedir dos números y una operación (+, -, *, /). Mostrar el resultado y validar división por cero. citeturn4search1  

**Ejercicio 1.3 – Validación de correo electrónico**  
Verificar que el correo contenga “@” y “.” en posiciones válidas. citeturn4search1  

**Ejercicio 1.4 – Validador de contraseña segura**  
Validar: mínimo 8 caracteres, una mayúscula, un número y un carácter especial (!@#$%^&*). Indicar qué criterios no se cumplen. citeturn4search1  

**Ejercicio 1.5 – Convertidor de unidades con menú**  
Menú: 1) Celsius→Fahrenheit, 2) Kilómetros→Millas, 3) Kilogramos→Libras. Mostrar con dos decimales. citeturn4search1  

---

### ✅ SECCIÓN 2: Implementación de Condicionales

**Ejercicio 2.1 – Clasificación de edades**  
Clasificar en: niño (0–12), adolescente (13–17), adulto (18–64), adulto mayor (65+). citeturn4search1  

**Ejercicio 2.2 – Menú de opciones básico**  
Menú: 1) Saludar, 2) Despedirse, 3) Salir. Usar `if-elif-else`. citeturn4search1  

**Ejercicio 2.3 – Calculadora con menú mejorado**  
Permitir múltiples operaciones sin salir del programa. Incluye 4 operaciones y opción de salir. citeturn4search1  

**Ejercicio 2.4 – Sistema de calificaciones con letras**  
Convertir nota (0–100) a letra: A (90–100), B (80–89), C (70–79), D (60–69), F (0–59). Validar rango. citeturn4search1  

**Ejercicio 2.5 – Simulador de descuentos por categoría**  
Categoría A=20%, B=15%, C=10% (otras: sin descuento). Mostrar total a pagar y ahorro. citeturn4search1  

---

### ✅ SECCIÓN 3: Uso de Ciclos `for` y `while`

**Ejercicio 3.1 – Generador de números pares**  
Pedir N y mostrar pares desde 1 hasta N con `for`. citeturn4search1  

**Ejercicio 3.2 – Acumulador numérico**  
Sumar números hasta que el usuario ingrese 0, luego mostrar la suma total. citeturn4search1  

**Ejercicio 3.3 – Búsqueda en lista de nombres**  
Buscar un nombre en una lista y mostrar si existe y su posición. citeturn4search1  

**Ejercicio 3.4 – Tabla de multiplicar interactiva**  
Generar tabla del 1 al 10 y preguntar si desea otra. Repetir hasta salir. citeturn4search1  

**Ejercicio 3.5 – Eliminador de duplicados en lista**  
Ingresar 10 números y mostrar lista sin duplicados usando ciclos y lista auxiliar (sin conjuntos). citeturn4search1  

---

### ✅ SECCIÓN 4: Gestión de Listas y Diccionarios

**Ejercicio 4.1 – Lista de compras**  
Agregar, eliminar y mostrar productos usando una lista. citeturn4search1  

**Ejercicio 4.2 – Directorio de contactos**  
Diccionario: nombre → teléfono. Permitir agregar, buscar y eliminar. citeturn4search1  

**Ejercicio 4.3 – Gestor de inventario**  
Lista de diccionarios con `nombre`, `precio`, `stock`. Actualizar precio buscando por nombre. citeturn4search1  

**Ejercicio 4.4 – Analizador estadístico**  
Ingresar números separados por comas y calcular: máximo, mínimo, promedio y suma. citeturn4search1  

**Ejercicio 4.5 – Comparador avanzado de listas**  
Ingresar dos listas y mostrar: comunes, únicos de la primera y únicos de la segunda (sin conjuntos). citeturn4search1  

---

### ✅ SECCIÓN 5: Creación y Uso de Funciones

**Ejercicio 5.1 – Generador de saludos personalizados**  
Función `saludar(nombre, hora)` con saludo según hora: días (5–12), tardes (13–19), noches (20–4). citeturn4search1  

**Ejercicio 5.2 – Calculadora de promedios**  
Función `calcular_promedio(lista)` que retorne el promedio. Validar lista vacía. citeturn4search1  

**Ejercicio 5.3 – Refactorización de menú de calculadora**  
Separar cada operación en una función y que el menú las invoque según opción. citeturn4search1  

**Ejercicio 5.4 – Detector de palíndromos**  
Función `es_palindromo(texto)` que ignore espacios, mayúsculas/minúsculas y signos de puntuación. citeturn4search1  

**Ejercicio 5.5 – Factorial recursivo**  
Función recursiva `factorial(n)` con validación para números negativos. citeturn4search1  

---

## 👨‍🏫 Autor
**Carlos Andrés Castro Jaramillo**  
Instructor – Desarrollo de Software citeturn4search1  
