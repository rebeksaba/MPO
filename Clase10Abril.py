numero = 1
print(numero)
numero = 10 * numero
print(numero)

if numero == 10 or numero%2 == 1:
    print("Es diez o impar")

elif numero != 10:
    print("No es diez")

else:
    print("No es un numero")

#Ejercicio 1 - Siempre negatifo, nunca positifo.
#Escribe un programa que pida al usuario un número entero y determine si es positivo o negativo.
#El programa debe imprimir un mensaje insicando el resultado.

numero = input("Introduce un número entero: ")
numero = int(numero)

#Comprobar si número es positivo
if numero >= 0:
    print("positivo")
else:
    print("negativo")

#Ejercicio 2 - Portero de discoteca.
#Escribe un programa que simule el trabajo de un portero de discoteca.
#El programa debe pedir al usuario su edad y determinar si puede entrar o no.
#Si la edad es menor de 18 años, el programa debe imprimir "No puedes entrar".  
#Si la edad es mayor o igual a 18 años, el programa debe imprimir "Puedes entrar".

edad = int(input("Cuantos años tienes? "))

if edad >= 18 and edad <= 60:
    print("Puedes pasar")
elif edad > 60:
    print("Vete a oldSchoolVeterans")
elif edad >= 16:
    print("Vete a KinderGarden")
else:
    print("Vete a casa")

#Ejercicio 3 - Pacman.
#Escribe un programa que pida al usuario dos números enteros correspondientes a la casilla que
#está Pacman (1º numero) y a la que está un fantasma (2º numero)
#luego debe recibir un texto con el formato "normal" o "caramelo"
#Si el texto es "normal" y los números son iguales, el programa debe imprimir
#"Pacman ha comido al fantasma". En cualquier otro caso, el programa debe imprimir
#"Pacman ha escapado".

pos_pacman = int(input("Cuál es la posición de pacman? "))
pos_fantasma = int(input("Cuál es la posición del fantasma? "))

if pos_pacman == pos_fantasma:
    estado_pacman =input("Como está Pacman? ")
    
    if estado_pacman == "caramelo":
        print("Pacman se ha comido al fantasma")
    else:
        print("Pacman ha sido atrapado")
else:
    print("Pacman ha escapado")

#Ejercicio 4 - Múltiplos de 3 y 5
#escribe un programa que pida al usuario un número entero y determine si es 
#múltiplo de 3 o de 5. El programa debe imprimir un mensaje indicando el resultado.
#Si el número es múltiplo de ambos, debe imprimir "Multiplo de 3 y 5".
#Si no es múltiplo de ninguno debe imprimir "No es múltiplo de 3 ni de 5".

numero_ent = int(input("Introduce un número entero: "))
if numero_ent % 15 == 0:
    print("Es múltiplo de 3 y de 5")
elif numero_ent % 3 == 0:
    print("Es múltiplo de 3")
elif numero_ent % 5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo de 3 ni de 5")

#Ejercicio 5 - Puede entrar en el servidor de Discord?
#Escribe un programa que pida un rol y una academia de estudios, si el rol es "alumno"
#y la academia es "Prometeo" el progrma debe darle acceso al servidor de discord oficial
#y al de los alumnos. Si el rol es "profesor" y la academia es "Prometeo" el programa debe
#darle acceso al servidor de Descord oficial pero no al de los alumnos. En cualquier otro caso
#el programa debe imprimir "No tienes acceso al servidor de Discord".

rol = input("Dime el rol del usuario: ").lower()
academia = input("En que academia estudias/trabajas? ").lower()

if rol == "estudiante" and academia == "prometeo":
    print("Access granted to: Official and Chill Discord")
elif rol == "profesor" and academia == "prometeo":
    print("Access granted to: Official Discord")
else:
    print("Enroll Prometeo to access to the best Discord servers")





