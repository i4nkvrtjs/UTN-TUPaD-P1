#Valentín Piñeyro
#Programación 1 TP N°5.1

#Ejercicio 1)

lista = list(range(4, 101, 4))

#Ejercicio 2)

lista = [1, 2, 3, 4, 5]

print(lista[-2])

#Ejercicio 3)

lista = []

lista.append("Primera")
lista.append("Segunda")
lista.append("Tercera")

print(lista)

#Ejercicio 4)

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#Ejercicio 5)

# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

#El programa usa la función remove para quitar de la lista el valor más alto (max()) de la misma. En este caso, el print imprimiría [8, 15, 3, 7]

#Ejercicio 6)

lista = list(range(10, 31, 5))

print(lista[0:2])

#Ejercicio 7)

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "uno"
autos[2] = "dos"

#Ejercicio 8)

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#Ejercicio 9)

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#Ejercicio 10)

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)