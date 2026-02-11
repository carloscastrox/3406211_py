#1. Cálculo de suma y promedio: Solicitar al usuario tres números enteros. Calcular y mostrar la suma total y el promedio de los números ingresados.

# Entradas
x = int(input("Ingrese el primer número entero: "))
y = int(input("Ingrese el segundo número entero: "))
z = int(input("Ingrese el tercer número entero: "))

# Proceso
sum = x + y + z
average = sum / 3

# Salidas
print("La suma total es:", sum)
print("El promedio es:", int(average))

"""
2. Área de un rectángulo: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.
3. Conversión de temperatura: Solicitar una temperatura en grados Celsius y convertirla a grados Fahrenheit.
4. Salario semanal: Solicitar la cantidad de horas trabajadas en la semana y el valor por hora. Calcular y mostrar el salario semanal.
5. Salario con horas extra: Solicitar horas trabajadas y valor por hora. Si el empleado trabajó más de 40 horas, las horas adicionales se pagan al 150%. Calcular el salario total.
6. Total de una venta: Solicitar el nombre del producto, el precio unitario y la cantidad comprada. Calcular y mostrar el valor total a pagar.
*7. Venta con descuento fijo: Solicitar el valor total de una compra. Si la compra supera los $200.000, aplicar un descuento del 10%. Mostrar el valor final a pagar.*
8. Venta con descuento por porcentaje: Solicitar el precio de un producto y el porcentaje de descuento. Calcular y mostrar el valor del descuento y el precio final.
9. Venta con IVA: Solicitar el valor de una venta sin impuestos. Calcular el IVA (19%) y mostrar el valor del IVA y el total con impuesto incluido.
10. Compra de varios productos: Solicitar la cantidad de productos comprados y el precio de cada uno. Calcular el total de la compra.
11. Comisión por ventas: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.
12. Comisión escalonada: Solicitar el valor de ventas mensuales. Si las ventas son mayores a $1.000.000, la comisión es del 10%; de lo contrario, es del 5%. Mostrar la comisión.
13. Promedio de notas: Solicitar tres notas de un estudiante. Calcular el promedio e indicar si aprueba (promedio mayor o igual a 3.0).
14. Nota final ponderada: Solicitar la nota de tres actividades: talleres (30%), examen parcial (30%) y examen final (40%). Calcular la nota definitiva.
15. Mayor de dos números: Solicitar dos números enteros y mostrar cuál de ellos es mayor o si son iguales.

16. Número par o impar: Solicitar un número entero e indicar si es par o impar.
17. Edad de una persona: Solicitar el año de nacimiento y el año actual. Calcular y mostrar la edad de la persona.
18. Clasificación por edad: Solicitar la edad de una persona e indicar si es menor de edad, adulto o adulto mayor.
19. Conversión de moneda: Solicitar un valor en pesos colombianos y convertirlo a dólares, usando una tasa de cambio ingresada por el usuario.
20. Cálculo de intereses simples: Solicitar el capital, la tasa de interés y el tiempo en meses. Calcular el interés simple y el valor total a pagar.
21. Cálculo de intereses compuestos: Solicitar el capital inicial, la tasa de interés y el número de períodos. Calcular el monto final.
22. Control de inventario: Solicitar la cantidad inicial de un producto en inventario, la cantidad vendida y la cantidad recibida. Calcular el inventario final.
23. Costo de envío: Solicitar el peso de un paquete. Si pesa hasta 5 kg, el envío cuesta $10.000; si pesa más, cuesta $20.000. Mostrar el valor del envío.
24. Factura de servicios públicos: Solicitar el consumo de agua en metros cúbicos y el valor por metro cúbico. Calcular el valor total de la factura.
25. Venta diaria de un almacén: Solicitar el número de ventas realizadas en el día y el valor de cada venta. Calcular el total vendido y el promedio por venta.

"""
