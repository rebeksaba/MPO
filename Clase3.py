import random
import math
#los import se ponen en la parte superior

#1. Longitud de una cadena
from builtins import PythonFinalizationError

nombre = "Rebeca"
apellido = "Sánchez"
print("Longitud del nombre: ", len(nombre))
print("Longitud del nombre: ", len(apellido))

#2. Convertir texto a mayusculas y minusculas
#upper
print("Esto soy yo en mayúsculas: ", nombre.upper())
#lower
print("Esto soy yo en minúsculas: ", apellido.lower())

#3. Slicing
print("Primeros 3 caracteres: ", nombre[:3])
print("Últimos 4 caracteres: ", nombre[-4:])


#4. Reemplazar palabras en una cadena
frase = "Me gusta Java"
print("Cambio la palabra: ", frase.replace("Java", "Python"))

#5. Verificar si una cadena existe en otra
print("Python" in frase)
nueva_frase= "Me gusta Python"
print("Cambio a Python", nueva_frase.lower())
print("Python" in nueva_frase)

#6. Unir varias palabras en una cadena
palabras = ["Hola" , "Mundo" , "en" , "Python"]
print("Frase completa con join: "," ".join(palabras))

#7. Split

oracion = "Python es divertido"
palabritas = oracion.split()
print("Lista de palabras de mi grupo: ", palabritas)

#8. Redondear un número decimal
numero = 3.1416
print("Mi número redondeado es:" , round(numero,2))

#9. Formateo de números decimales
precio = 19.99
print("Precio con dos decimales: {:.2f}".format(precio))

#10. Obtener el valor ASCII de un carácter
print("Esto es el código ASCII de 'A': ", ord('A'))
#cada letra tiene un código diferente, para temas de criptografía.

#11. Elevar al cuadrado
numero_al_cuadrado = 5
print("5 al cuadrado es: ", numero_al_cuadrado ** 2)
#la potencia se pone con el número, si quiero elevar al cubo sería **3

#12. Raíz cuadrada
print("Raíz cuadrada de 25 es: ", 25 ** 0.5)

numerito = 100
raiz = math.sqrt(numerito)
print("Raíz cuadrada de 100 es: ", raiz)

#13. Divisiones enteras y resto

print("División normal : ", 10/3)
print("División entera : ", 10//3)
print("Resto : ", 10%3)

#14. Generar un número aleatorio

print("Numero aleatorio entre 1 y 10: ", random.randint(1,10))


#15. Convertir números a cadenas y viceversa
numerajo = 300
texto = str(numerajo)
print("Convertido a texto, soy: ", texto)

cadena = "200"
numerajo = int(cadena)
print("COnvertido a número soy: ", numerajo)
print(numerajo+texto)

#16. Redondear hacia arriba y hacia abajo
print("Redondeo hacia arriba del número 3.6: ", math.ceil(3.6))
print("Redondeo hacia abajo del número 3.2: ", math.floor(3.2))

#17. Convedrtir una lista en un conjunto, es decir, eliminar duplicados
numeroides = [1,2,3,3,4,5,5]
sin_duplicados = set(numeroides)
print("La lista de numeroides sin duplicados es: ",sin_duplicados)

#18. Repetir una cadena
print("Money!" * 3)

#19. Tipo de dato
dato = 3.14
print("El tipo de variable de dato es: ", type(dato))


#20. Combinar cadenas y variables en un print
name = "Rebeca"
edad = 31
print(f"Hola, soy {name} y tengo {edad} años.")
