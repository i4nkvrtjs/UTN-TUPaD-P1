#Valentín Piñeyro
#Programación 1 Práctico 1

#1)
print("Ejercicio 1)")
print("Hola Mundo!")

#2)
print("Ejercicio 2)")
nombre = input("Cuál es tu nombre? ")

print(f"Hola, ", nombre)

#3)
print("Ejercicio 3)")
nombre = input("Dime tu nombre ")
apellido = input("Dime tu apellido ")
edad = input("Dime tu edad ")
lugar = input("Dime tu lugar de residencia ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

#4)
print("Ejercicio 4)")
import math

radio = float(input("Dime el radio "))
area = round(math.pi * radio ** 2, 2)
perimetro = round(2 * math.pi * radio, 2)

print(f"El area del círculo es de {area} y el perímetro es de {perimetro}")

#5)
print("Ejercicio 5)")
segundos = int(input("Dime la cantidad de segundos "))
horas = round(segundos / 3600, 1)

print(f"{segundos} segundos equivalen a {horas} horas")

#6)
print("Ejercicio 6)")
num = int(input("Dime un número entero "))
producto = 0

for i in range(1, 11, 1):
    producto = num * i
    print(f"{num} * {i} = {producto}")

#7)
print("Ejercicio 7)")
num1 = 0
num2 = 0

while num1 == 0:
    num1 = int(input("Ingrese el primer número "))
    if num1 == 0:
        print("El número no puede ser 0")

while num2 == 0:
    num2 = int(input("Ingrese el segundo número "))
    if num2 == 0:
        print("El número no puede ser 0")

suma = num1 + num2
division1 = num1 / num2
division2 = num2 / num1
multiplicacion = num1 * num2
resta1 = num1 - num2
resta2 = num2 - num1

print(f"El resultado de sumar ambos números es: {suma}")
print(f"El resultado de multiplicar ambos números es: {multiplicacion}")
print(f"El resultado de dividir el primer número por el segundo es: {division1}")
print(f"El resultado de dividir el segundo número por el primero es: {division2}")
print(f"El resultado de restarle el primer número al segundo es: {resta2}")
print(f"El resultado de restarle el segundo número al primero es: {resta1}")

#8)
print("Ejercicio 8)")
peso = float(input("Ingrese su peso en kilogramos "))
altura = float(input("Ingrese su altura en metros "))
masa = round(peso / (altura ** 2), 1)

print(f"Su índice de masa corporal es de: {masa}")

#9)
print("Ejercicio 9)")
celsius = float(input("Ingrese la temperatura en Celsius "))
farenheit = round((9 / 5) * celsius + 32, 1)

print(f"{celsius} grados Celsius esquivalen a {farenheit} grados Farenheit")

#10)
print("Ejercicio 10)")
num1 = int(input("Ingrese el primer número "))
num2 = int(input("Ingrese el segundo número "))
num3 = int(input("Ingrese el tercer número "))
promedio = round((num1 + num2 + num3) / 3, 2)

print(f"El promedio de los números ingresados es {promedio}")
