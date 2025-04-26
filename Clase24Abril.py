## ESTRUCTURA DE CONTROL DE REPETICIÓN##

#Ejercicio 1 - Contador
#Escribe un programa que pida al usuario un número entero positivo e imprima los
#números desde el 0 hasta ese número (incluido). El programa debe imprimir los
#números en cada iteración.

numero1 = int(input("Introduce un número entero positivo"))
for i in range (0,numero1+1):
    print(i)

#Ejercicio 2 - Contador de números pares
#Escribe un programa que pida al usuario un número entero positivo y cuente cuántos
#números pares hay desde 0 hasta ese número (incluido). 
#El programa debe imprimir el resultado.

numero2 = int(input("Introduce un número entero positivo"))
pares = 0
for i in range (0,numero2+1):
    if i % 2 == 0:
        pares = pares + 1

print (f"Número de pares: {pares}")

#Ejercicio 3 - Cuenta atrás
#Escribe un programa que pida al usuario un número entero positivo y realice una
#cuenta atrás desde ese número hasta 0. El programa debe imprimir cada número en la
#cuenta atrás.

numero3 = int(input("Introduce un número entero positivo"))
for i in range (numero3,-1,-1):
    print(i)


#Ejercicio 4 - Factorial
#Escribe un programa que pida al usuario un número entero positivo y calcule su
#factorial. El programa debe imprimir el resultado. El factorial de un número n se define
#como el producto de todos los números enteros desde 1 hasta n.
#Por ejemplo, el factorial de 5 (5!) es: 5 * 4 * 3 * 2 * 1 = 120.

numero4 = int(input("Introduce un número entero positivo"))
factorial = 1
for i in range (numero4,1,-1):
    factorial = factorial * i

print(f"El factorial de {numero4} es {factorial}")


#Ejericio 5 - Múltiple de 3 o 5
#Escribe un programa que pida al usuario un número entero positivo e imprima
#solamente los números múltiplos de 3 o de 5 dentro de ese rango.
#Si el número es múltiplo de 3, imprime el número seguido de el mensaje "es múltiplo de
#3". Si el número es múltiplo de 5, imprime el número seguido del mensaje "es múltiplo
#de 5". Si el número es múltiplo de ambos no debes imprimir nada.

numero5 = int(input("Introduce un número entero positivo"))

for i in range (numero5+1):
    if i % 3 == 0 and i % 5 ==0:
        continue
    elif i % 3 == 0:
        print(f"{i} es múltiplo de 3")
    elif i % 5 ==0:
        print(f"{i} es múltiplo de 5")

#Ejercicio 6 - Triángulo de asteriscos
#Escribe un programa que pida al usuario un número entero positivo y dibuje un triángulo
#de asteriscos con la altura especificada.

altura = int(input("Introduce la altura del triángulo"))
base = ""

for i in range (1,altura,+1):
    base = base + "*"
    print(base)

#Ejercicio 7 - Tabla de multiplicar
#Escribe un programa que pida al usuario un número entero positivo y 
#muestre la tabla de multiplicar de ese número.

numero7 = int(input("Introduce un número entero positivo"))

for i in range(1,11):
    print(f"{numero7} x {i} = {numero7*i}")


#Ejercicio 8 - Cuadrado con cruz
#Escribe un programa que pida al usuario un número entero positivo
#impar y dibuje un cuadrado de x con una cruz en el medio.

dimension = int(input("Introduce un número positivo impar que indique la dimensión del cuadrado:\n"))

for i in range(dimension):
    for j in range(dimension):
        if i == 0 or i == dimension-1:
            print("x"*dimension,end="")
            break
        if j == 0 or j == dimension-1 or j == i or j+i == dimension-1:
            print("x",end="")
        else:
            print(" ",end="")
    print()

