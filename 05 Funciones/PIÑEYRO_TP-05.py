#Trabajo Práctico N°5

#Valentín Piñeyro

#Ejercicio 1)

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#Ejercicio 2)

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario(input("Como te llamas? "))

#Ejercicio 3)

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal(input("Dime tu nombre "), input("Dime tu apellido "), input("Dime tu edad "), input("Dime donde vives "))

# Ejercicio 4)

from math import pi

def calcular_area_circulo(radio):
    area = round(pi * radio ** 2, 2)
    print(f"El área del círculo es {area}")

def calcular_perimetro_circulo(radio):
    perimetro = round(pi * radio * 2, 2)
    print(f"El perímetro del círculo es {perimetro}")

radio = float(input("Ingrese el radio "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#Ejercicio 5)

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = int(input("Ingrese la cantidad de segundos "))
horas = round(segundos_a_horas(segundos), 2)
print(f"{segundos} segundos equivale a {horas} horas")

#Ejercicio 6)

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabla_multiplicar(int(input("Ingrese un número ")))

#Ejercicio 7)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def operaciones_basicas(a, b):
    tupla = suma(a, b), resta(a, b), resta(b, a), multiplicacion(a, b), division(a, b), division(b, a)
    print(f"""
La suma de los números es: {tupla[0]}
La resta del segundo número sobre el primero es: {tupla[1]}
La resta del primer número sobre el segundo es: {tupla[2]}
La multiplicación de los números es: {tupla[3]}
La división del primer número con el segundo es: {tupla[4]}
La división del segundo número con el primero es: {tupla[5]}
""")
    return tupla

#Ejercicio 8)

def calcular_imc(peso, altura):
    imc = round(peso / altura ** 2, 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos "))
altura = float(input("Ingrese su altura en metros "))
print(f"Su índice de masa corporal es de {calcular_imc(peso, altura)}")

#Ejercicio 9)

def celsius_a_farenheit(celsius):
    farenheit = celsius * (9 / 5) + 32
    return farenheit

celsius = float(input("Ingrese la temperatura en °C "))
farenheit = celsius_a_farenheit(celsius)
print(f"{celsius}°C equivalen a {farenheit}°F")

#Ejercicio 10)

def calcular_promedio(a, b, c):
    return round((a + b + c) / 3, 2)

num1 = int(input("Ingrese el primer número "))
num2 = int(input("Ingrese el segundo número "))
num3 = int(input("Ingrese el tercer número "))
print(f"El promedio de los números ingresados es: {calcular_promedio(num1, num2, num3)}")












