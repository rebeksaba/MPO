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
    print(f"Nota media evaluación {i}: {suma_notas/num_notas}")
        


