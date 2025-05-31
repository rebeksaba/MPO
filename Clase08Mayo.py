#Ejercicio 9 - Suma acumulativa
#Escribe un programa que pida al usuario una serie de números enteros y calcule la suma
#acumulativa de estos números. El programa debe seguir pidiendo números hasta que el usuario 
#ingrese un 0. Al final, imprime la suma total.

print("Introduce números para sumarlos:")
numero = int(input())
resultado = 0

while numero != 0:
    resultado += numero
    numero = int(input())

print(f"El resultado es {resultado}")

#Ejercicio 10 - Akinator numérico
#Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine
#el número. El programa debe dar pistas al usuario si el níumero es mayor o menor que el número elegido.
#El programa debe seguir pidiendo números hasta que el usuario adivine el número correcto.

import random

random_num = random. randint(1,100)

user_num = int(input("Introduce un número del 1 al 100: "))

while random_num != user_num:
    if user_num > random_num:
        print("El número es demasiado alto")
    else:
        print("🤏")
    user_num = int(input("Introduce un número del 1 al 100: "))
print("Enhorabuena")

#Ejercicio 11 - Media de notas
#Escribe un programa que pida al ususario cuantas evaluaciones hay que calificar.
#Seguidamente se recibirán  ese número de series de notas (números decimales entre 0 y 10) y
#calcule la media de esas notas. El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1.
#Al final, imprime la media.

#Introduce evaluaciones: 3

evaluaciones = int(input("Introduce el número de evaluaciones"))

for i in range(evaluaciones):
    nota = float(input("Introduce la siguiente nota: "))
    num_notas = 0
    suma_notas = 0
    while nota != -1:
        num_notas += 1
        suma_notas += nota
        nota = float(input("Introduce la siguiente nota: "))
    print(f"Nota media evaluación {i+1}: {suma_notas/num_notas}")
        

#Ejercicio 12 - Mayor y menor
#Escribe un programa que puda al usuario una serie de números enteros y determine cuál es el mayor
#y cuál es el  menor. El programa debe seguir pidiendo números hasta que el usuario ingrese un 0 al final,
#imprime el mayor y el menor.

mayor = float('-inf')
menor = float('inf')
numero_12 = int(input("Introduce un valor (0 para terminar): "))

while numero_12 != 0:
    if numero_12 > mayor:
        mayor = numero_12
    if numero_12 < menor:
        menor = numero_12
        
    numero_12 = int(input("Introduce un valor (0 para terminar): "))

print(f"Mayor: {mayor} Menor: {menor}")

#Ejercicio 13 - Número de cifras
#Escribe un programa que pida al usuario una serie de números enteros positivos hasta 
#la introducción de un valor -1 para cada número debe contar cuántas cifras tiene. 
#El programa debe imprimir la longitud de cada número. 
#No podéis usar la función len() para contar las cifras ni convertir el número a cadena.

numero_13 = int(input("Introduce un número ( -1 para finalizar): "))

while numero_13 != -1:
    cifras = 1
    copia_num = numero_13
    while numero_13 > 9:
        cifras += 1
        numero_13 //= 10

    print(f"El número de dígitos de {copia_num} es {cifras}")
    numero_13 = int(input("Introduce un número (-1 para acabar): "))

#Ejercicio 15 - Banca online
#Escribe un programa que simule una cuenta bancaria. 
#El programa debe permitir al usuario realizar las siguientes operaciones:

#1. Ingresar dinero
#2. Retirar dinero
#3. Consultar saldo
#4. Salir
#Inicializa el saldo en 0 y permite al usuario realizar operaciones hasta que decida salir.
#'''

saldo = 0
opcion = -1

while opcion != 4
    print("Escoge una opción:")
    print("1.Ingresar dinero:")
    print("2.Retirar dinero:")
    print("3.Consultar saldo:")
    print("4.Salir:")

    opcion = int(input())

    if opcion == 1:
        saldo += int(input("Qué cantidad deseas ingresar? "))
    elif opcion == 2:
        saldo -= int(input("Qué cantidad deseas retirar? "))
    elif opcion == 3:
        print (f"Tu saldo es {saldo}")
    else:
        print("Escoge una opción de la 1 a la 4")