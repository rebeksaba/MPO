#Ejercicio 1: Operaciones numéricas complejas
#Define cinco variables


#cntrol + / para poner como comentario el código y que no interfiera con los siguientes ejercicios
# num1, num2, num3, num4, num5 = 10, 3, 2.5, 7.2, 4+2j
# resultado = (f"Potencia:{num1 ** num2}, División entera: {num1//num2},  "
#              f"Módulo: {num1%num2}, Multiplicación: {num3*num4}, Complejo: {num5}")
# print(resultado)
# oracion = (f"Hola mundo: {num3*num1}, Suma:"
#            f"{num3+num5}")
# print(oracion)


#Ejercicio 2

# num_int, num_float = 8, 3.5
# cadena1, cadena2, cadena3 = "Resultado: ", "La suma es ", "y la división es "
# resultado = (cadena1 + "" + cadena2 + "" + cadena3 + "" + str(num_int/num_float) +
#             cadena3 + "" + str(num_int/num_float))
## en las comillas se podría poner cosas, pero no es necesario
#
# print(resultado)

#Ejercicio 3. Manipulación avanzada de cadenas

# cadena = " Esto es una cadena para manipular  "
# nueva_cadena = cadena.strip().upper().split()
# print(nueva_cadena)

##.strip quita los huecos
##.upper pone mayúsculas
##.split divide la cadena

#Ejercicio 4: Índices y subcadenas
#Define una cadena extensa (mínimo 50 caracteres).
#Obtén varias subcadenas usando la indexación por rangos (slicing) y genera una nueva cadena combinando esstas subcedenas en orden inverso.
#Imprime la nueva cadena resultante.

# cadena_extensa = "Python es un super lenguaje que me re encanta"
# subcadena = cadena_extensa [0:6] + "" + cadena_extensa [11:20]
# resultado = subcadena [::-1]
# print(resultado)


#Ejercicio 5. Formato y conversión numérica
#Define variables numéricas (entero, flotante, complejo)


# entero, flotante, complejo = 12, 345.23976, 5+3j
# formato = (f"Entero: {entero}, Flotante {flotante:.2f}, Notación científica: {flotante:.2e}"
#            f"Notación científica: {flotante:.2e}, Complejo: {complejo}")
# print(formato)

#Ejercicio 6. Operaciones combinadas entre números y cadenas.

# num_a, num_b = 15, 4
# cad_a, cad_b = "La multiplicación da: " , "y el resto es: "
# resultado = f"{cad_a}{num_a * num_b}, {cad_b}{num_a % num_b}"
# print(resultado)


#Ejercicio 7. Cálculo del área y perímetro

# largo, ancho, radio, altura = 10, 5, 3, 4
# area_rectangulo = largo * ancho
# perimetro_rectangulo = 2 * (largo+ancho)
#
# area_circulo = 3.14 * radio ** 2
# perimetro_circulo = 2 * 3.14 * radio
#
# area_triangulo = (largo*altura)/2
#
#
# resultado = (f"Area de un rectangulo: {area_rectangulo}, Perímetro del rectángulo {perimetro_rectangulo},"
#              f"Area de un circulo: {area_circulo}, Perimetro del circulo: {perimetro_circulo},"
#              f"\nArea del triangulo: {area_triangulo}")
#
# print(resultado)



#Ejercicio 8. Análisis de texto complejo

parrafo = "Soy un ejemplo de párrafo largo de narices para ocupar el espacio que quiero"
caracteres = len(parrafo)
palabroides = len(parrafo.split())
mayusculas = parrafo.upper()
resultado = (f"Total de caracteres: {caracteres}, "
             f"\ntotal de palabras: {palabroides},"
             f"\nTexto en mayusculas: {mayusculas}")
print(resultado)


#Ejercicio 9. Fórmula cuadrática

#Ejercicio 10.







