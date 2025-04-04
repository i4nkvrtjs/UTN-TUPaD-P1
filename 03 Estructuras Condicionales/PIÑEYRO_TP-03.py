#Trabajo Práctico N°3

#Valentín Piñeyro

#Ejercicio 1)

edad = int(input("Ingrese su edad "))

if edad >= 18:
    print(f"Es mayor de edad")

#Ejercicio 2)

nota = float(input("Ingrese su nota "))

if nota >= 6:
    print(f"Aprobado")
elif nota < 0:
    print("Nota ingreada no es válida")
else:
    print(f"Desaprobado")

#Ejercicio 3)

num = int(input("Ingrese un número par "))

if num % 2 == 0:
    print(f"Ha ingresado un número par")
else:
    print(f"Por favor, ingrese un número par")

#Ejercicio 4)

edad = int(input("Ingrese su edad "))

if edad >= 0 and edad < 12:
    print(f"Usted pertenece a la categoría Niño/a")
elif edad >= 12 and edad < 18:
    print(f"Usted pertenece a la categoría Adolescente")
elif edad >= 18 and edad < 30:
    print(f"Usted pertenece a la categoría Adulto/a joven")
elif edad < 0:
    print("Edad ingresada no es válida")
else:
    print(f"Usted pertenece a la categoría Adulto/a")

#Ejercicio 5)

contraseña = input("Ingrese una contraseña (mínimo 8 caracteres, máximo 14 caracteres) ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print(f"Ha ingresado una contraseña correcta")
else:
    print(f"Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6)

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print(numeros_aleatorios)
    print(f"La moda es {moda}, la mediana es {mediana} y la media es {media}")
    print(f"Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print(numeros_aleatorios)
    print(f"La moda es {moda}, la mediana es {mediana} y la media es {media}")
    print(f"Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print(numeros_aleatorios)
    print(f"La moda es {moda}, la mediana es {mediana} y la media es {media}")
    print(f"Sin sesgo")
else:
    print(numeros_aleatorios)
    print(f"La moda es {moda}, la mediana es {mediana} y la media es {media}")

#Ejercicio 7)

frase = input("Ingrese una frase o palabra ")
vocales = ["a", "e", "i", "o", "u"]

if len(frase) > 0 and (frase[-1].lower() in vocales):
    print(f"{frase}!")
else:
    print(frase)

#Ejercicio 8)

nombre = input("Ingrese su nombre ")
num = int(input("""Ingrese la opción deseada: 
    1 para ver su nombre en mayúsculas
    2 para ver su nombre en minúsculas
    3 para ver su nombre con la primer letra mayúscula 
    """))

if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.title())
else:
    print("Por favor, ingrese un número correcto")

#Ejercicio 9)

magnitud = float(input("Ingrese la magnitud del terremoto "))

if magnitud > 0 and magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
elif magnitud == 0:
    print("El número no puede ser 0")
else:
    print("Ingrese un número positivo")

#Ejercicio 10)

treintaYUno = [1, 3, 5, 7, 8, 10, 12]
treinta = [4, 6, 9, 11]

hemisferio = input("En qué hemisferio se encuentra? N/S ")

if hemisferio.lower() == "n" or hemisferio.lower() == "s":
    pass
else:
    hemisferio = input("En qué hemisferio se encuentra? N/S ")

mes = int(input("Ingrese el número de mes "))

if mes >= 1 and mes <= 12:
    pass
else:
    mes = int(input("Por favor, ingrese un mes válido "))

dia = int(input("Ingrese el número de día "))

if mes in treintaYUno and (dia >= 1 and dia <= 31):
    pass
elif mes in treinta and (dia >= 1 and dia <= 30):
    pass
elif mes == 2 and (dia >= 1 and dia <= 29):
    pass
else:
    dia = int(input("Por favor, ingrese un día válido "))

if hemisferio.lower() == "n":
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        print("Es Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        print("Es Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        print("Es Verano")
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        print("Es Otoño")
else:
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        print("Es Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        print("Es Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        print("Es Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        print("Es Primavera")















