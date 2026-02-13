#Cálculo de área y perímetro usando math

print("========================================")
print("Cálculo de área y perímetro usando math")
print("Creado por Carlos Andrés Castro Jaramillo")
print("=========================================\n")

import math
def a2():
        try:
            radio = float(input("Ingresa el radio del círculo: "))
            #area = pi * radio ^ 2
            area = math.pi * math.pow(radio,2)
            # perimetro  * pi * radio
            perimetro = 2 * math.pi * radio

            print("Área: ", round(area, 2))
            print("Perimetro: ", round(perimetro,2))

        except ValueError:
                print("Debes ingrear un número válido")

if __name__ == "__main__":
        a2()