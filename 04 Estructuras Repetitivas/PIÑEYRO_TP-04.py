#Trabajo Práctico N°4

#Valentín Piñeyro

#Ejercicio 1)

for i in range(101):
    print(i)

#Ejercicio 2)

num = int(input("Ingrese un número entero "))
digitos = 1

while num > 9:
    num = num // 10
    digitos += 1

print(f"El número tiene {digitos} dígitos")

#Ejercicio 3)

num1 = int(input("Ingrese el primer número entero "))
num2 = int(input("Ingrese el segundo número entero "))
suma = 0

if num1 > num2:
    for i in range(num2 + 1, num1):
        suma += i
elif num1 == num2:
    print("los números no pueden ser iguales")
else:
    for i in range(num1 + 1, num2):
        suma += i

print(f"La suma de los números comprendidos entre ambos números ingresados es {suma}")

#Ejercicio 4)

num = int(input("Ingrese un número (0 para salir) "))
sum = num

while num != 0:
    num = int(input("Ingrese otro número (0 para salir) "))
    sum += num

print(f"La suma de los número ingresados es {sum}")

#Ejercicio 5)

from random import randrange

num_aleatorio = int(randrange(10))
intentos = 1
num = int(input("Adivine el número entre 0 y 9 "))

while num != num_aleatorio:
    num = int(input("Incorrecto, intente otro número "))
    intentos += 1

print(f"Correcto! Le tomó {intentos} intentos")

#Ejercicio 6)

for i in range(100, 0, -2):
    print(i)

#Ejercicio 7)

num = int(input("Ingrese un número entero positivo "))
sum = 0

for i in range(num + 1):
    sum += i

print(f"La suma de los números entre 0 y el número ingresado es de {sum}")

#Ejercicio 8)

CANTIDAD_DE_NUMEROS = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(1, CANTIDAD_DE_NUMEROS + 1):
    num = int(input(f"Ingrese el {i}° número entero "))
    if num == 0:
        pass
    elif num > 0:
        positivos += 1
    else:
        negativos += 1
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"""
    Se ingresaron {positivos} números positivos
    Se ingresaron {negativos} números negativos
    Se ingresaron {pares} números pares
    Se ingresaron {impares} números impares
    """)

#Ejercicio 9)

CANTIDAD_DE_NUMEROS = 100
sum = 0

for i in range(1, CANTIDAD_DE_NUMEROS + 1):
    num = int(input(f"Ingrese el {i} número entero "))
    sum += num

media = sum / CANTIDAD_DE_NUMEROS
print(f"La media de los valores ingresados es {media}")

#Ejercicio 10)

num = int(input("Ingrese un número "))
numRev = 0
negativo = False

if num < 0:
    num = -num
    negativo = True

while num >= 1:
    digito = num % 10
    numRev = numRev * 10 + digito
    num = num // 10

if negativo:
    numRev = -numRev

print(numRev)
    



