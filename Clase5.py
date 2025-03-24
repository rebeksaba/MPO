# Ejercicios - Tipos básicos, Números, Cadenas y Booleanos
# Parte 1: Booleanos y Operaciones con Números


# Ejercicio 1: Evaluación de Expresiones Booleanas
# 📌 Objetivo: Evaluar expresiones numéricas que devuelvan valores booleanos.
# Crea variables con expresiones matemáticas y convierte los resultados en booleanos.
# Muestra el valor booleano de cada una.

expresion1 = 10>5
expresion2 = 7+3==10
expresion3 = 4*2==9
expresion4 = 20<15
print(expresion1, expresion2, expresion3, expresion4)

# Ejercicio 2: Operaciones Matemáticas con Booleanos
# 📌 Objetivo: Descubrir cómo Python trata los valores True y False en operaciones matemáticas.
# Suma True + True y False + True.
# Multiplica True * 10 y False * 50.
# Muestra los resultados y explica qué ocurre.

print(True+True)  #-->True es igual a 1; False es igual a 0
print(True-True)
print(False+True)
print(False+False)
print(False-False)
print(True*10)
print(False*50)

# Ejercicio 3: Conversión entre Tipos Básicos
# 📌 Objetivo: Convertir entre tipos de datos (números, cadenas y booleanos).
# Convierte un número en cadena y muéstralo.
# Convierte una cadena numérica en un entero.
# Convierte un booleano en un número.



# Ejercicio 7: Evaluación de Expresiones Lógicas
# 📌 Objetivo: Trabajar con operadores lógicos (and, or, not).
# Evalúa expresiones lógicas combinando números y operadores lógicos.
# Muestra los resultados.

print(10>5 and 3<8)
print(5==5 or 2>10)
print(4==4 and 3>1)
print(not(4==4 and 3>1))