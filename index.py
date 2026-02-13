# index.py
# Creado por Carlos Andrés Castro Jaramillo



import os # Interactúa con el sistema operativo (archivos, directorios, rutas, variables de entorno).
import sys  #Maneja la configuración y el entorno del intérprete de Python (argumentos de línea de comandos, rutas de módulos).
import subprocess #Ejecuta comandos externos y programas, controlando sus entradas/salidas y errores.


while True:
    #Encabezado
    print("=========================================")
    print("Taller 1 - Algortimos Básicos en Python")
    print("By Carlos Andrpes Castro Jaramillo")
    print("Menú Principal")
    print("=========================================")

    for i in range(1, 26):
        print(f"{i}. Ejecutar Algoritmo{i}")
    print("0. Salir\n")

    opcion = input("Seleccione una opción: ")

    if opcion == "0":
        print("Saliendo ...")
        break

    if opcion.isdigit() and 1 <= int(opcion) <= 25:
        archivo = f"a{opcion}.py"

        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
        else:
            print(f"No existe {archivo}")
    
    else:
        print("Opción no válida")

    input("\n Presiona ENTER para continuar ...")