# import random
# import math
# #los import se ponen en la parte superior
#
# #1. Longitud de una cadena
# from builtins import PythonFinalizationError
#
# nombre = "Rebeca"
# apellido = "Sánchez"
# print("Longitud del nombre: ", len(nombre))
# print("Longitud del nombre: ", len(apellido))
#
# #2. Convertir texto a mayusculas y minusculas
# #upper
# print("Esto soy yo en mayúsculas: ", nombre.upper())
# #lower
# print("Esto soy yo en minúsculas: ", apellido.lower())
#
# #3. Slicing
# print("Primeros 3 caracteres: ", nombre[:3])
# print("Últimos 4 caracteres: ", nombre[-4:])
#
#
# #4. Reemplazar palabras en una cadena
# frase = "Me gusta Java"
# print("Cambio la palabra: ", frase.replace("Java", "Python"))
#
# #5. Verificar si una cadena existe en otra
# print("Python" in frase)
# nueva_frase= "Me gusta Python"
# print("Cambio a Python", nueva_frase.lower())
# print("Python" in nueva_frase)
#
# #6. Unir varias palabras en una cadena
# palabras = ["Hola" , "Mundo" , "en" , "Python"]
# print("Frase completa con join: "," ".join(palabras))
#
# #7. Split
#
# oracion = "Python es divertido"
# palabritas = oracion.split()
# print("Lista de palabras de mi grupo: ", palabritas)
#
# #8. Redondear un número decimal
# numero = 3.1416
# print("Mi número redondeado es:" , round(numero,2))
#
# #9. Formateo de números decimales
# precio = 19.99
# print("Precio con dos decimales: {:.2f}".format(precio))
#
# #10. Obtener el valor ASCII de un carácter
# print("Esto es el código ASCII de 'A': ", ord('A'))
# #cada letra tiene un código diferente, para temas de criptografía.
#
# #11. Elevar al cuadrado
# numero_al_cuadrado = 5
# print("5 al cuadrado es: ", numero_al_cuadrado ** 2)
# #la potencia se pone con el número, si quiero elevar al cubo sería **3
#
# #12. Raíz cuadrada
# print("Raíz cuadrada de 25 es: ", 25 ** 0.5)
#
# numerito = 100
# raiz = math.sqrt(numerito)
# print("Raíz cuadrada de 100 es: ", raiz)
#
# #13. Divisiones enteras y resto
#
# print("División normal : ", 10/3)
# print("División entera : ", 10//3)
# print("Resto : ", 10%3)
#
# #14. Generar un número aleatorio
#
# print("Numero aleatorio entre 1 y 10: ", random.randint(1,10))
#
#
# #15. Convertir números a cadenas y viceversa
# numerajo = 300
# texto = str(numerajo)
# print("Convertido a texto, soy: ", texto)
#
# cadena = "200"
# numeral = int(cadena)
# print("Convertido a número soy: ", numeral)
#
#
# #16. Redondear hacia arriba y hacia abajo
# print("Redondeo hacia arriba del número 3.6: ", math.ceil(3.6))
# print("Redondeo hacia abajo del número 3.2: ", math.floor(3.2))
#
# #17. Convedrtir una lista en un conjunto, es decir, eliminar duplicados
# numeroides = [1,2,3,3,4,5,5]
# sin_duplicados = set(numeroides)
# print("La lista de numeroides sin duplicados es: ",sin_duplicados)
#
# #18. Repetir una cadena
# print("Money!" * 3)
#
# #19. Tipo de dato
# dato = 3.14
# print("El tipo de variable de dato es: ", type(dato))
#
#
# #20. Combinar cadenas y variables en un print
# name = "Rebeca"
# edad = 31
# print(f"Hola, soy {name} y tengo {edad} años.")
#
# #----------------------------EJERCICIOS CON ESTAS UTILIDADES COMBINADAS------------------------------------#
#
# #1. Generador de nombres de usuario.
#
# #Pide al usuario su nombre y apellido.
#
# nombre1 = input("Escribe tu nombre:")
# apellido1 = input("Escribe tu apellido")
#
# #Genera un nombre de usuario en minúsculas, sin espacios.
#
# nombreUsuario= (nombre1 + apellido1).lower()
#
# #Añade un número aleatorio al final
#
# numeroRandom= random.randint(0, 100)
#
# #Muestra el nombre de usuario generado
#
# user= f"{nombreUsuario}{numeroRandom}"
#
# print(f"Tu nombre de usuario es: {user}")
#
# #2. Analizador de frases
#
# #Pide al usuario que ingrese una frase.
#
# fraseUsuario= input("Escribe una frase:")
#
# #Muestra la cantidad de caracteres de la frase
#
# print("Longitud de la frase: ", len(fraseUsuario))
#
# #Indica si la frase contiene la palabra "Python".
#
# print("¿Encuestras la palabra Python?" in frase)
#
# #Convierte la frase a mayúsculas.
#
# print("Esta es la frase en mayúsculas: ", fraseUsuario.upper())
#
# #Muestra la frase invertida.
#
# print("Esta es la frase invertida: ", fraseUsuario[::-1])
#
# #3. Cálculo de descuentos.
#
# #Pide al usuario el precio de un producto.
#
# precio_producto= float(input("Escribe el precio del producto:"))
#
# #Aplica un 15% de descuento.
# descuento= precio_producto * 0.15
# precio_final= precio_producto - descuento
#
# #Muestra el precio final con dos decimales
# print("Aplicado el descuento: {:.2f}€".format(precio_final))
#
# #Muestra el precio redondeado hacia arriba.
# print("Precio redondo: ", math.ceil(precio_final))
#
# #4. Generador de etiquetas de productos.
#
# #Pide el nombre de un producto y su precio.
# nombre_producto= input("Producto")
# preciodelproducto= float(input("Precio"))
#
# #Convierte el nombre del producto a mayúsculas
# print("PRODUCTO MAYUS: ", nombre_producto.upper())
#
# #Muestra el precio con dos decimales
# print("Precio del Producto: {:.2f}€".format(preciodelproducto))
#
# #Genera un código basado en el valor ASCII de la primera letra del producto.
# print("Esto es el código ASCII de: ", ord(nombre_producto[0]))
#
# #5. Conversión de tipos y manipulación de listas
#
# #Pide al usuario una lista de números separados por comas.
#
# listadenumeros= input(["Escribe números separados por comas"])
#
#  #Convierte cada número a entero
#
#
#  #Elimina los números repetidos
# sin_repetidos = set(listadenumeros)
# print("La lista de numeros sin duplicados es: ",sin_repetidos)
#
# #Muestra la lista ordenada sin duplicados
#
#
# #6. Creación de mensajes personalizados
#
# #Pide al ususario su nombre, edad y ciudad.
# tu_nombre = input ("Tu nombre")
# tu_edad = input("Tu edad")
# localidad = input("Tu localidad")
#
#
# #Muestra un mensaje con toda la información usando f-strings
# print(f"Hola, soy {tu_nombre} , tengo {tu_edad} años y vivo en {localidad}.")
#
# #Si la edad es menor de 18, redondea hacia arriba para calcular la mayoría de edad.
# #NO ME SALE
# #mayor_de_edad= math.ceil(tu_edad / 18) * 18
#
# #7. Generador de contraseñas aleatorias
# #Crea una contraseña segura con la primera letra de tu nombre un número aleatorio y un símbolo especial.
# nombre_1= input("Escribe tu nombre")
# contraseña= f"{nombre[0].upper()}{random.randint(0,999)}&"
#
# print(f"Tu nueva contraseña:{contraseña}")
#
# #8. Verificación de nombres en listas
# #Pide al usuario su nombre y verifica si está en una lista de invitados.
#
# invitados= ["Julia", "Francisco", "Miguel", "Rebeca"]
# su_nombre= input("Su nombre")
#
# #----------------No sé hacerlo----------
# #Muestra su posición en la lista.
#
#
# #9. Manipulación de nombres
# #Pide al usuario su nombre y apellido
#
# nombre_user= input("Nombre")
# apellido_user= input("Apellido")
#
# #Convierte el nombre a minúsculas, el apellido a mayúsculas.
# #Genera un alias combinando las primeras 3 letras de cada uno.
#
# #print(f"Alias: ", {nombre_user.lower()[:3])} + {apellido_user.upper()[:3]}) yo lo he formulado así pero no sirve
#
# alias= nombre_user[:3].lower() + apellido_user[:3].upper()
# print(f"tu alias es: {alias}")
#
#
# #10. Formatear y mostrar datos matemáticos
#
# #Pide al usuario un número flotante
# numeroflotante= float(input("Pon un número decimal:"))
#
# #Muestra el número redondo, su cuadrado y su raíz cuadrada
#
# print("Número redondeado:" , round(numeroflotante, 2))
# print("Su cuadrado es:" , numeroflotante**2)
# print("Su raíz cuadrada es:" , numeroflotante**0.5)

