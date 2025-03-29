# #Ejercicio 1: Operaciones numéricas complejas
# #Define cinco variables numéricas distintas (int, float, complex) y realiza diversas
# #operaciones matemáticas (potenciación, división entera, módulo). Imprime los resultados
# #~formateados en una cadena clara y descriptiva.
# from Clase2 import multiplicacion
#
# ##cntrol + / para poner como comentario el código y que no interfiera con los siguientes ejercicios
#
#
# num1, num2, num3, num4, num5 = 10, 3, 2.5, 7.2, 4+2j
# resultado = f"Potencia:{num1 ** num2}, División entera: {num1//num2},  "\
#               f"Módulo: {num1%num2}, Multiplicación: {num3*num4}, Complejo: {num5}"
# print(resultado)
# oracion = (f"Hola mundo: {num3*num1}, Suma:"
#             f"{num3+num5}")
# print(oracion)
#
#
# #Ejercicio 2: Combinación de cadenas y números.
# #Define dos variables numéricas (int, float) y tres cadenas diferentes. Genera una nueva
# #cadena combinando texto con el resultado de operaciones aritméticas entre estas variables.
# #Usa conversión explícita (str()) para insertar valores numéricos en la cadena final.
#
# num_int, num_float = 8, 3.5
# cadena1, cadena2, cadena3 = "Resultado: ", "La suma es ", "y la división es "
# resultado2 = (cadena1 + "" + cadena2 + "" + cadena3 + "" + str(num_int/num_float) +
#              cadena3 + "" + str(num_int/num_float))
# ## en las comillas se podría poner cosas, pero no es necesario
#
# print(resultado)
#
# #Ejercicio 3: Manipulación avanzada de cadenas.
# #Crea una cadena larga que contenga espacios en blanco al inicio, final, y en medio. Realiza
# #varias operaciones encadenadas como eliminar espacios extremos, convertirlo a mayúsculas,
# #dividir la cadena en varias subcadenas usando un separador específico.
#
# cadenalarga = " Soy una cadena larga que tengo espacios "
# cadena_retocada = cadenalarga.strip().upper().split()
# print(cadena_retocada)
#
# ##.strip quita los huecos al principio y al final
# ##.upper pone mayúsculas
# ##.split divide la cadena por palabras
#
# #Ejercicio 4: Índices y subcadenas
# #Define una cadena extensa (mínimo 50 caracteres). Obtén varias subcadenas usando la
# #indexación por rangos (slicing) y genera una nueva cadena combinando estas subcedenas
# #en orden inverso. Imprime la nueva cadena resultante.
#
# ##definición cadena extensa
# cadena_extensa = "Soy una cadena extensa y tengo que tener 50 caracteres para este ejercicio"
# ##Creación de la subcadena, [0:6] extrae los primeros 6 caracteres de la cadena "Soy un"
# ## [11:20] extrae los caracteres desde la posición 11 hasta la posición 19 "cadena ex"
# subcadena = cadena_extensa [0:6] + "" + cadena_extensa [11:20]
# ##Revertir la subcadena, invierte los caracteres
# resultado4 = subcadena [::-1]
# ##Imprime el resultado
# print(resultado4)
#
#
# #Ejercicio 5. Formato y conversión numérica
# #Define variables numéricas (entero, flotante, complejo). crea una cadena con formato
# #avanzado (f-strings) que muestre estos números con precisión definida (dos decimales,
# #notación científica, etc). Evita concatenar directamente números y texto.
#
# entero, flotante, complejo = 5, 9.8, 5+14j
# ##Aquí se utiliza una f-string para formatear e incluir las variables directamente en una cadena de texto.
# ##{flotante:.2f} formatea el valor de flotante con dos decimales 9,80
# ##Notación científica: {flotante:.2e} Muestra el valor de flotante en notación científica
# ##{complejo} Inserta el número complejo tal cual
# cadena_avanzada = (f"Entero: {entero} , Flotante {flotante:.2f}, Notación científica: {flotante:.2e} "
#                    f"Complejo: {complejo}")
# ##Imprime el resultado
# print(cadena_avanzada)
#
#
# #Ejercicio 6: Operaciones combinadas entre números y cadenas.
# #Define dos variables numéricas enteras y dos cadenas. Realiza cálculos matemáticos
# #diversos y genera una cadena formateada que explique cada operación (sumas, restas, multiplicaciones,
# #módulo) claramente utilizando métodos de cadenas.
#
# num_a, num_b = 10, 20
# cad_a, cad_b = "El resultado de: " , "la operación es:"
# suma = num_a + num_b
# resta = num_a - num_b
# multiplicacion = num_a * num_b
# modulo = num_a % num_b
#
# resultado6 = (f"{cad_a} la suma entre {num_a} y {num_b}, {cad_b}: {suma}\n"
#               f"{cad_a} la resta entre {num_a} y {num_b}, {cad_b}: {resta}\n"
#               f"{cad_a} la multiplicación entre {num_a} y {num_b}, {cad_b}: {multiplicacion}\n"
#               f"{cad_a} el módulo entre {num_a} y {num_b}, {cad_b}: {modulo}")
# print(resultado6)
#
# ##Ejemplo de clase:
#
# num_a, num_b = 15, 4
# cad_a, cad_b = "La multiplicación da: " , "y el resto es: "
# resultado = f"{cad_a}{num_a * num_b}, {cad_b}{num_a % num_b}"
# print(resultado)
#
#
# #Ejercicio 7: Cálculo del área y perímetro.
# #Define variables numéricas que representen dimensiones (largo, ancho, radio, altura).
# #Calcula el área y perímetro de distintas figuras geométricas (rectángulo, círculo, triángulo)
# #y presenta todos los resultados claramente en una sola cadena formateada usando
# #conversiones explícitas.
#
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
# resultado7 = (f"Area de un rectangulo: {area_rectangulo}, Perímetro del rectángulo {perimetro_rectangulo},"
#              f"Area de un circulo: {area_circulo}, Perimetro del circulo: {perimetro_circulo},"
#              f"\nArea del triangulo: {area_triangulo}")
#
# print(resultado7)
#
#
#
# #Ejercicio 8: Análisis de texto complejo.
# #Define una cadena extensa que represente un párrafo completo. Utilizando únicamente métodos
# #de cadenas y funciones integradas (len, upper, split), obtén el número total de caracteres
# #palabras y el resultado de transformar el texto completamente a mayúsculas, presentándolo
# #claramente en una cadena nueva.
#
# parrafo = "Soy un ejemplo de párrafo largo de narices para ocupar el espacio que quiero"
# caracteres = len(parrafo)
# palabroides = len(parrafo.split())
# mayusculas = parrafo.upper()
# resultado = (f"Total de caracteres: {caracteres}, "
#              f"\ntotal de palabras: {palabroides},"
#              f"\nTexto en mayusculas: {mayusculas}")
# print(resultado)
#
#
# #Ejercicio 9: Fórmula cuadrática.
# #Dados tres números que representan los coeficientes (a, b, c) de una ecuación cuadrática,
# #resuelve la fórmula cuadrática para obtener las raíces reales o comlejas. Imprime
# #claramente en una cadena formateada los coeficientes y las raíces encontradas.
#
# a, b, c = 1, -3, 2
# discriminante = (b ** 2 - 4 * a * c) ** 0.5
# raiz1 = (-b + discriminante) / (2 * a)
# raiz2 = (-b - discriminante) / (2 * a)
# resultado = f"Coeficientes: a={a}, b={b}, c={c}. Raíces: {raiz1}, {raiz2}"
# print(resultado)
#
#
# #Ejercicio 10. Manejo y transformación de datos personales.
# #Crea variables para representar datos personales (nombre, edad, peso, altura). Calcula el
# #índice de masa corporal (IMC) sin usar bucles, y presenta un resumen detallado y formateado
# #de todos estos datos personales, incluyendo el IMC con dos decimales.
# #
# nombre, edad, peso, altura = "Rebeca", 31, 75, 1.65
# imc= peso / altura ** 2
# resultado10 = f"Nombre: {nombre}, Edad: {edad}, Peso: {peso}, Altura {altura} m, IMC: {imc:.2f}"
# print(resultado10)








