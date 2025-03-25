# Ejercicios - Tipos básicos, Números, Cadenas y Booleanos
# Parte 1: Booleanos y Operaciones con Números
from Clase3 import cadena

# Ejercicio 1: Evaluación de Expresiones Booleanas
# 📌 Objetivo: Evaluar expresiones numéricas que devuelvan valores booleanos.
# Crea variables con expresiones matemáticas y convierte los resultados en booleanos.
# Muestra el valor booleano de cada una.

# expresion1 = 10>5
# expresion2 = 7+3==10
# expresion3 = 4*2==9
# expresion4 = 20<15
# print(expresion1, expresion2, expresion3, expresion4)

# Ejercicio 2: Operaciones Matemáticas con Booleanos
# 📌 Objetivo: Descubrir cómo Python trata los valores True y False en operaciones matemáticas.
# Suma True + True y False + True.
# Multiplica True * 10 y False * 50.
# Muestra los resultados y explica qué ocurre.

# print(True+True)  #-->True es igual a 1; False es igual a 0
# print(True-True)
# print(False+True)
# print(False+False)
# print(False-False)
# print(True*10)
# print(False*50)

# Ejercicio 3: Conversión entre Tipos Básicos
# 📌 Objetivo: Convertir entre tipos de datos (números, cadenas y booleanos).
# Convierte un número en cadena y muéstralo.
# Convierte una cadena numérica en un entero.
# Convierte un booleano en un número.

numero = 123
cadena = str(numero)
print(cadena)
cadena_numerica = "456"
numero_convertido = int(cadena_numerica)
print(numero_convertido)

print(int(True)) # 1
print(int(False)) # 0


# Ejercicio 4: Propiedades de las Cadenas
# 📌 Objetivo: Manipular cadenas y explorar sus propiedades.
# Crea una cadena con tu nombre.
# Muestra el primer y último carácter.
# Muestra la longitud de la cadena.
# Convierte la cadena a mayúsculas y minúsculas.

nombre = "Rebeca"
print(nombre[0]) #R
print(nombre[-1]) #a

print(len(nombre)) # 6

print(nombre.upper()) #REBECA
print(nombre.lower()) #rebeca


# Ejercicio 5: Operaciones con Cadenas y Números
# 📌 Objetivo: Realizar operaciones matemáticas con cadenas y números.
# Concatenar cadenas con números usando str().
# Multiplicar una cadena para repetirla varias veces.

edad = 25
mensaje = "Tengo" + str(edad) + "años"
print(mensaje) #Tengo 25 años

repetido = "Hola"*3
print(repetido) #Hola Hola Hola

# Ejercicio 6: Operaciones con Caracteres y Códigos ASCII
# 📌 Objetivo: Explorar caracteres y su representación en ASCII.
# Obtén el código ASCII de la letra 'A'.
# Convierte un número en su carácter ASCII correspondiente.

codigo =ord('A')
print(codigo) # 65

letra= chr(66)
print(letra) #B



# Ejercicio 7: Evaluación de Expresiones Lógicas
# 📌 Objetivo: Trabajar con operadores lógicos (and, or, not).
# Evalúa expresiones lógicas combinando números y operadores lógicos.
# Muestra los resultados.

print(10>5 and 3<8)
print(5==5 or 2>10)
print(4==4 and 3>1)
print(not(4==4 and 3>1))

##CLASE 25/03/25

# Créame un diccionario
persona = {
    "nombre" : "Rebeca",
    "edad" : 31,
    "registrado" : True

}
print(persona)
#Accedeme a un valor por su clave
print(persona["edad"])

#Añadir una nueva clave-valor
persona["ciudad"] = "Vurgos"
persona["Número de hijos"] = 3
print(persona)

#Cambiar el valor de una clave
persona["ciudad"] = "Burgos"
persona ["Número de hijos"] = 7
print(persona)

#Eliminar una clave
# del persona["registrado"]
# print(persona)

#Comprobar si una clave ya existe
existe_rebeca = "Rebeca" in persona["nombre"]
print(existe_rebeca)

#Comprobar dos valores booleanos
es_menor_y_registrado = persona["edad"]<18 and persona["registrado"]
print(es_menor_y_registrado)

#Usar NOT con un booleano
no_veo_registro = persona["registrado"]
print(no_veo_registro)

#Creame un conjunto a partir de una lista con duplicados
numeritos = [1,2,3,5,7,2,6,8,4]

#convierto a conjunto. PORQUE ASÍ ELIMINO DUPLICIDADES
conjuntito = set(numeritos)
print(conjuntito)

#Comparar si dos colecciones tienen los mismos elementos unicos
coleccion_a = set([1,2,2,3])
coleccion_b = set([3,2,1])

mismos_elementitos = coleccion_a == coleccion_b
print(mismos_elementitos)

