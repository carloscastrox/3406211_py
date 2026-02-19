print("=======================================================================")
print("Taller 2: ")
print("Creado por Carlos Andrés Castro Jaramillo")
print("=====================================================================\n")


#List
#Basándose en una lista de frutas, deseo una nueva lista que contenga solo las frutas con la letra "e" en el nombre
# Imprima frutas que inicien con una letra.
# list = ["Manzana","Banano","Arandanos","Fresa","Cereza"]
# newlist = []
# for x in list:
#     if "e" in x:
#         newlist.append(x)    
# print(newlist)

list = ["Manzana","Banano","Arandanos","Fresa","Cereza"]
#newlist = [x for x in list]
newlist = [x.upper() if x != "Banano" else "Fresa" for x in list]
newlist.sort(reverse = True)
print(newlist)
print(list)

#for x in range(len(list)):
#   print(list[x])

#print(x) for x in  list]


# Tuple
# tuple = ("Manzana","Banano","Arandanos","Fresa","Cereza")
# print(tuple[-4:-1])

# Set
# set = {"Manzana","Banano","Arandanos","Fresa","Cereza"}
# print("Fresa" not in set)

# Dictionaries
# car = {
#     "brand": "Toyota",
#     "color": ["Gris","Rojo","Azul"],
#     "model": 2024,
#     "ref": "Yaris",
#     "electric": True
# }
# print(len(car))
