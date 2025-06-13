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

def contactos():
    contactos = {}

    while True:
        opcion = int(input("Bienvenidx a tus contactos.\nElije la opción deseada: 1- Ingresar nuevo contacto, 2- Buscar contacto, 3- Salir "))
        
        if opcion == 1:
            if len(contactos) <= 5:
                nombre = input("Ingresa el nombre del contacto nuevo ")
                numero = input("Ingresa el número del contacto nuevo ")
                contactos[nombre] = numero
            else:
                print("Ya tienes 5 contactos guardados.")
        elif opcion == 2:
            if contactos:
                nombreBuscado = input("Ingresa el contacto a buscar ")
                if nombreBuscado in contactos:    
                    print(contactos[nombreBuscado])
                else:
                    print("Contacto no encontrado.")
            else:
                print("No hay contactos.")
        elif opcion == 3:
            break
        else:
            print("Opción inválida")

contactos()

#Ejercicio 5)

frase = input("Ingresa una frase ")

palabras = frase.split()
palabrasUnicas = set(palabras)

frecuencia = {}

for palabra in palabras:
    palabra = palabra.lower()
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

for palabra, cantidad in frecuencia.items():
    print(f"{palabra}: {cantidad}")

#Ejercicio 6)

def alumnos():
    alumnos = {}

    while True:
        opcion = int(input("Ingresa la opción deseada: 1- Agregar alumno, 2- Calcular promedio, 3- Salir "))

        if opcion == 1:
            nombre = input("Ingresa el nombre del alumno: ")
            nota1 = int(input("Ingresa la primer nota: "))
            nota2 = int(input("Ingresa la segunda nota: "))
            nota3 = int(input("Ingresa la tercer nota: "))
            notas =  nota1, nota2, nota3
            alumnos[nombre] = tuple(notas)
        elif opcion == 2:
            nombreBuscado = input("Ingresa el nombre del alumno a buscar: ")
            if nombreBuscado in alumnos:
                print(f"Promedio: {sum(alumnos[nombreBuscado]) / 3}")
            else:
                print("Alumno no encontrado.")
        elif opcion == 3:
            break
        else:
            print("Opción inválida.")
    
alumnos()

#Ejercicio 7)

aprobadosParcial1 = {1, 3, 5, 7, 9, 4}
aprobadosParcial2 = {2, 4, 6, 8, 10, 5}

print("Aprobaron ambos parciales:")
print(aprobadosParcial1 & aprobadosParcial2)
print("Aprobaron solo uno de los dos parciales:")
print(aprobadosParcial1 ^ aprobadosParcial2)
print("Aprobaron al menos un parcial:")
print(aprobadosParcial1 | aprobadosParcial2)

#Ejercicio 8)

def stock():
    stock = {
        "manzana": 10,
        "papa": 9,
        "zanahoria": 7,
        "miel": 12
    }


    while True:
        opcion = int(input("Ingresa la opción deseada: 1- Consultar stock, 2- Agregar unidades, 3- Agregar producto, 4- Mostrar stock actual, 5- Salir "))
        
        if opcion == 1:
            nombreBuscado = input("Ingresa el nombre del producto a buscar: ").lower()
            if nombreBuscado in stock:
                print(f"{nombreBuscado}: {stock[nombreBuscado]}")
            else:
                print("Producto no encontrado.")
        elif opcion == 2:
            nombreBuscado = input("Ingresa el nombre del producto a buscar: ").lower()
            if nombreBuscado in stock:
                unidades = int(input("Ingresa la cantidad de unidades a agregar: "))
                stock[nombreBuscado] += unidades
                print(f"{nombreBuscado}: {stock[nombreBuscado]}")
            else:
                print("Producto no encontrado.")
        elif opcion == 3:
            nombreAgregar = input("Ingresa el nombre del producto a agregar: ")
            unidades = int(input("Ingresa la cantidad de unidades del producto nuevo: "))
            stock[nombreAgregar] = unidades
        elif opcion == 4:
            print(stock)
        elif opcion == 5:
            break
        else:
            print("Opción inválida.")

stock()

#Ejercicio 9)

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miercoles", "12:00"): "Almuerzo con mamá",
    ("jueves", "16:30"): "Fútbol",
    ("viernes", "21:00"): "Cita con Juan",
    ("sabado", "14:40"): "Llevar a Laura al médico",
    ("domingo", "09:45"): "Dormir"
}

dia = input("Qué día quieres consultar? ")
hora = input("Qué hora quieres consultar?(formato XX:XX) ")

if (dia, hora) in agenda:
    print(f"El día {dia} a las {hora}hs tienes {agenda[dia, hora]}")
else:
    print("No tienes nada ese día en ese horario.")

#Ejercicio 10)

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}
invertido = {valor: clave for clave, valor in original.items()}

print(f"Original: {original}")
print(f"Invertido: {invertido}")