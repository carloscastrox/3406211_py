# 📘 Taller 2: Python — Estructuras de Control y Funciones

Este repositorio contiene un **taller práctico** de Python enfocado en:
- Manejo de variables y entrada de datos
- Condicionales
- Ciclos `for` y `while`
- Listas y diccionarios
- Creación y uso de funciones  

---

## 🎯 Objetivo
Fortalecer la lógica de programación mediante la implementación de **ejercicios progresivos** organizados por secciones temáticas. 

---

## ✅ Requisitos
- Python 3.x (recomendado)
- Editor de código (VS Code u otro)

---

## ▶️ ¿Cómo ejecutar?
Si tu repositorio incluye un archivo `index.py` como punto de entrada, puedes ejecutarlo así:  

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
Validar que la edad sea un número positivo.  

**Ejercicio 1.2 – Calculadora básica**  
Pedir dos números y una operación (+, -, *, /). Mostrar el resultado y validar división por cero.   

**Ejercicio 1.3 – Validación de correo electrónico**  
Verificar que el correo contenga “@” y “.” en posiciones válidas.   

**Ejercicio 1.4 – Validador de contraseña segura**  
Validar: mínimo 8 caracteres, una mayúscula, un número y un carácter especial (!@#$%^&*). Indicar qué criterios no se cumplen. 

**Ejercicio 1.5 – Convertidor de unidades con menú**  
Menú: 1) Celsius→Fahrenheit, 2) Kilómetros→Millas, 3) Kilogramos→Libras. Mostrar con dos decimales. 

---

### ✅ SECCIÓN 2: Implementación de Condicionales

**Ejercicio 2.1 – Clasificación de edades**  
Clasificar en: niño (0–12), adolescente (13–17), adulto (18–64), adulto mayor (65+).  

**Ejercicio 2.2 – Menú de opciones básico**  
Menú: 1) Saludar, 2) Despedirse, 3) Salir. Usar `if-elif-else`.  

**Ejercicio 2.3 – Calculadora con menú mejorado**  
Permitir múltiples operaciones sin salir del programa. Incluye 4 operaciones y opción de salir.  

**Ejercicio 2.4 – Sistema de calificaciones con letras**  
Convertir nota (0–100) a letra: A (90–100), B (80–89), C (70–79), D (60–69), F (0–59). Validar rango.   

**Ejercicio 2.5 – Simulador de descuentos por categoría**  
Categoría A=20%, B=15%, C=10% (otras: sin descuento). Mostrar total a pagar y ahorro.   

---

### ✅ SECCIÓN 3: Uso de Ciclos `for` y `while`

**Ejercicio 3.1 – Generador de números pares**  
Pedir N y mostrar pares desde 1 hasta N con `for`.   

**Ejercicio 3.2 – Acumulador numérico**  
Sumar números hasta que el usuario ingrese 0, luego mostrar la suma total.  

**Ejercicio 3.3 – Búsqueda en lista de nombres**  
Buscar un nombre en una lista y mostrar si existe y su posición.  

**Ejercicio 3.4 – Tabla de multiplicar interactiva**  
Generar tabla del 1 al 10 y preguntar si desea otra. Repetir hasta salir.  

**Ejercicio 3.5 – Eliminador de duplicados en lista**  
Ingresar 10 números y mostrar lista sin duplicados usando ciclos y lista auxiliar (sin conjuntos).  

---

### ✅ SECCIÓN 4: Gestión de Listas y Diccionarios

**Ejercicio 4.1 – Lista de compras**  
Agregar, eliminar y mostrar productos usando una lista.  

**Ejercicio 4.2 – Directorio de contactos**  
Diccionario: nombre → teléfono. Permitir agregar, buscar y eliminar.  

**Ejercicio 4.3 – Gestor de inventario**  
Lista de diccionarios con `nombre`, `precio`, `stock`. Actualizar precio buscando por nombre.  

**Ejercicio 4.4 – Analizador estadístico**  
Ingresar números separados por comas y calcular: máximo, mínimo, promedio y suma.  

**Ejercicio 4.5 – Comparador avanzado de listas**  
Ingresar dos listas y mostrar: comunes, únicos de la primera y únicos de la segunda (sin conjuntos).  

---

### ✅ SECCIÓN 5: Creación y Uso de Funciones

**Ejercicio 5.1 – Generador de saludos personalizados**  
Función `saludar(nombre, hora)` con saludo según hora: días (5–12), tardes (13–19), noches (20–4).   

**Ejercicio 5.2 – Calculadora de promedios**  
Función `calcular_promedio(lista)` que retorne el promedio. Validar lista vacía.   

**Ejercicio 5.3 – Refactorización de menú de calculadora**  
Separar cada operación en una función y que el menú las invoque según opción.  

**Ejercicio 5.4 – Detector de palíndromos**  
Función `es_palindromo(texto)` que ignore espacios, mayúsculas/minúsculas y signos de puntuación.  

**Ejercicio 5.5 – Factorial recursivo**  
Función recursiva `factorial(n)` con validación para números negativos. 


### ✅ SECCIÓN 6: MINI-TALLER INTEGRADOR
**Sistema de gestión de biblioteca**
Descripción del sistema:
Desarrollar un programa completo en Python para gestionar los libros de una biblioteca, aplicando todos los conceptos aprendidos en las secciones anteriores. El sistema debe permitir realizar operaciones básicas de mantenimiento de un catálogo bibliográfico.

**Requisitos funcionales:**
1.	Estructura de datos: Utilizar una lista de diccionarios para almacenar la información de los libros. Cada libro debe contener: id (numérico autoincremental), título, autor, año de publicación y estado de disponibilidad (True/False).
2.	Funciones principales:
  o	agregar_libro(): Permite registrar un nuevo libro validando que el año sea numérico y mayor a 1900.
  o	mostrar_libros(): Muestra todos los libros en formato legible: "ID: 1 - 'Cien años de soledad' (Gabriel García Márquez, 1967) [Disponible]"
  o	buscar_libro(): Permite buscar libros por título o autor, mostrando coincidencias parciales.
  o	prestar_libro(id): Cambia el estado de disponibilidad a False si el libro existe y está disponible.
  o	devolver_libro(id): Cambia el estado de disponibilidad a True.
  o	eliminar_libro(id): Elimina un libro solo si no está prestado actualmente.
  o	menu_principal(): Implementa un menú interactivo con las opciones anteriores utilizando while para repetir hasta que se seleccione salir.
3.	Funciones adicionales desafiantes:
  o	libros_por_autor(autor): Lista todos los libros de un autor específico.
  o	estadisticas(): Muestra estadísticas del sistema: cantidad total de libros, libros disponibles y libros prestados.
  o	exportar_a_txt(): Guarda todos los libros en un archivo de texto llamado "biblioteca.txt".

**Entregables esperados:**
*	Archivo Python ejecutable con el nombre biblioteca.py.
* Código completo con comentarios explicativos en cada función.
---

## 👨‍🏫 Autor
**Carlos Andrés Castro Jaramillo**  
Instructor – Desarrollo de Software
