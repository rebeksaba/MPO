# ------------------------------------------------------------------------------------------------------------------
#  1 TIPOS NUMÉRICOS EN PHYTON


# ENTEROS (int)
# Los enteros son números sin decimales, pueden ser positivos o negativos.
numero_entero = 43
numero_negativo = -12

print("Numero entero es:", numero_entero)
print("Me imprimo un número negativo",numero_negativo)
print("Quiero imprimir qué tipo de dato tengo", type(numero_negativo))
print("Quiero imprimir qué tipo de dato tengo", type(numero_entero))

# DECIMALES (float)
#Los  números flotantes son aquellos que tienen decimales.
numero_decimal =3.14
temperatura = -3.5
print("Número decimal:",numero_decimal)
print("Hace estos grados",temperatura)
print("Quiero imprimir qué tipo de dato tengo AHORA", type(numero_decimal))


# NUMEROS COMPLEJOS (complex)
#Los números complejos tienen una parte real y una imaginaria (se usa "j")
num_complejo=2 + 3j
print("Imprime el número complejo siguiente:",num_complejo)
print("Imprime la parte real:",num_complejo.real,"| Parte imaginaria:",num_complejo.imag)
print("Dime que tipo de dato soy:", type(num_complejo))

# OPERACIONES MATEMÁTICAS BÁSICAS CON NÚMEROS
suma = 10 + 5
resta = 3 - 2
multiplicacion = 2*3
division = 10/5
division_entera = 10//3
modulo = 10%3
potencia = 2**3
print("Aquí tengo el valor de la suma:",suma)
print("Aquí tengo el valor de la resta:",resta)
print("Aquí tengo el valor de la multiplicacion:",multiplicacion)
print("Aquí tengo el valor de la division:",division)
print("Aquí tengo el valor de la division entera:",division_entera)
print("Aquí tengo el valor del modulo:",modulo)
print("Aquí tengo el valor de la potencia:",potencia)
