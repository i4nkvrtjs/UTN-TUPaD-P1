# #Programación 1 TP N°7

# #Valentín Piñeyro

#Ejercicio 1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"El factorial de {i} es: {factorial(i)}")

#Ejercicio 2)

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

num = int(input("Ingrese la posición de la serie fibonacci deseada: "))

for i in range(0, num):
    print(f"En la posición {i + 1} el valor es: {fibonacci(i)}")

#Ejercicio 3)

def potencia(base, expo):
    if expo == 0:
        return 1
    else:
        return base * potencia(base, expo - 1)

base = int(input("Ingrese el número base: "))
expo = int(input("Ingrese el exponente: "))

print(f"El número {base} elevado al exponente {expo} da como resultado: {potencia(base, expo)}")

#Ejercicio 4)

def decimal_a_binario(num):
    if num < 0:
        return "El número debe ser un entero positivo"
    
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

#Ejercicio 5)

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1 : -1])

#Ejercicio 6)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
    
#Ejercicio 7)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
#Ejercicio 8)

def contar_digito(numero, digito):
    if digito < 0 or digito > 9:
        return 0
    
    if numero == 0:
        return 0
    
    ult_digito = numero % 10
    cuenta = 1 if digito == ult_digito else 0

    return cuenta + contar_digito(numero // 10, digito)



        


