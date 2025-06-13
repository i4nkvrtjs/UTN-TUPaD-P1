#Programación 1
#TP N° 7 Datos Complejos
#Valentín Piñeyro

#Ejercicio 1)

precios_frutas = {
    "Banana": 1200,
    "Ananá": 2500,
    "Melón": 3000,
    "Uva": 1450
}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#Ejercicio 2)

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

#Ejercicio 3)

lista = list(precios_frutas.keys())

#Ejercicio 4)

class Persona:
    def __init__(nombre, pais, edad):
        print(f"¡Hola! Soy {nombre}, vivo en {pais} y tengo {edad} años")

#Ejercicio 5)

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return math.pi * self.radio * 2

#Ejercicio 6)

def balanceado(string):
    pila = []
    pares = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for caracter in string:
        if caracter in "([{":
            pila.append(caracter)
        elif caracter in ")]}":
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
    return not pila

string1 = "([{}])"
string2 = "()[]{}"
string3 = "{](})["

print(balanceado(string1))
print(balanceado(string2))
print(balanceado(string3))

#Ejercicio 7)

class Cola:
    def __init__(self):
        self.cola = []
    
    def encolar(self, cliente):
        self.cola.append(cliente)
        print(f"{cliente} agregado a la cola.")
    
    def desencolar(self):
        if self.cola:
            atendido = self.cola.pop(0)
            print(f"Cliente atendido: {atendido}.")
            return atendido
        else:
            print("No hay clientes en la cola.")
            return None

    def mostrar_siguiente(self):
        if self.cola:
            print(f"El próximo cliente es: {self.cola[0]}.")
            return self.cola[0]
        else:
            print("No hay clientes en la cola.")
            return None

cola = Cola()
cola.encolar("Pablo")
cola.encolar("Ian")
cola.desencolar()
cola.mostrar_siguiente()

#Ejercicio 8)

class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    
class ListaEnlazada():
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print(f"{valor} insertado al inicio.")

    def mostrar_lista(self):
        actual = self.cabeza
        if not actual:
            print("La lista no contiene elementos.")
            return
        while actual:
            print(actual.valor, end = " -> ")
            actual = actual.siguiente
        print("None")

lista = ListaEnlazada()

lista.insertar(1)
lista.insertar(2)
lista.mostrar_lista()

#Ejercicio 9)

class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    
class ListaEnlazada2():
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print(f"{valor} insertado al inicio.")

    def mostrar_lista(self):
        actual = self.cabeza
        if not actual:
            print("La lista no contiene elementos.")
            return
        while actual:
            print(actual.valor, end = " -> ")
            actual = actual.siguiente
        print("None")
    
    def invertir(self):
        anterior = None
        actual = self.cabeza

        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        
        self.cabeza = anterior

lista2 = ListaEnlazada2()

lista2.insertar(11)
lista2.insertar(22)
print("Lista original:")
lista2.mostrar_lista()

lista2.invertir()
print("Lista invertida:")
lista2.mostrar_lista()