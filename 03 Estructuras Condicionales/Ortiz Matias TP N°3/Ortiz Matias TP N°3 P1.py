""" 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. """

""" edad_mayor= 18
edad = int(input("Ingrese su edad: "))
if edad > edad_mayor:
    print("Es mayor de edad!.") """

""" 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”.  """

""" nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado!")
else:
    print("Desaprobado!") """

""" 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
operador de módulo (%) en Python para evaluar si un número es par o impar.  """

""" num = int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("El numero ingresado es par!")
else:
    print("El numero ingresado no es par!") """

""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años.  """

""" edad = int(input("Ingrese su edad: "))
if edad < 12 and edad >= 1:
    print("Ud pertenece a la categoria de Niño!")
elif edad >= 12 and edad < 18:
    print("Ud pertenece a la categoria de Adolescente!")
elif edad >= 18 and edad < 30:
    print("Ud pertence a la categoria de Adulto joven!")
elif edad >= 30:
    print("Ud pertence a la categoria de Adulto !")
elif edad <= 0:
    print("ERROR - ingrese su edad!")
 """

""" 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string.  """

""" password = input("ingrese una contraseña de entre 8 y 14 caracteres: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta!") 
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") """

""" 6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
 """
""" import random 
from statistics import mode, median, mean 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

promedio = mean(numeros_aleatorios) 
num_medio = median(numeros_aleatorios)
num_moda = mode(numeros_aleatorios)
print("De estos numeros: ", numeros_aleatorios)
print(" El numero promedio es: ", promedio)
print(" El numero medio es: ", num_medio)
print(" El numero que mas se repite es: ", num_moda) """

""" 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla. """

""" frase = input("Introduce una frase o palabra: ")
if frase[-1].lower() in 'aeiou':
   
    frase += '!'
print(frase) """

""" 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas.  """

""" nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. ")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("Seleccione una opcion"))

if opcion == 1:
    mayus = nombre.upper()
    print("", mayus)
elif opcion == 2:
    minus = nombre.lower()
    print("", minus)
elif opcion == 3:
    mayusprimera = nombre.title()
    print("", mayusprimera) """

""" 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).  """

""" magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Es un terremoto Muy leve.")
elif magnitud >= 3 and magnitud < 4:
    print("Es un terremoto leve.")
elif magnitud >= 4 and magnitud < 5:
    print("Es un terremoto Moderado.")
elif magnitud >= 5 and magnitud < 6:
    print("Es un terremoto Fuerte.")
elif magnitud >= 6 and magnitud < 7:
    print("Es un terremoto Muy Fuerte.")
elif magnitud >= 7:
    print("Es un terremoto Extremo.") """

""" 10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano.  """

""" hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

def estacion_norte(mes, dia):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        return "Verano"
    else:
        return "Otoño"

def estacion_sur(mes, dia):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        return "Invierno"
    else:
        return "Primavera"

if hemisferio == "N":
    estacion = estacion_norte(mes, dia)
elif hemisferio == "S":
    estacion = estacion_sur(mes, dia)
else:
    estacion = "Hemisferio no válido"

print(f"En el hemisferio {hemisferio} y la fecha proporcionada, la estación es: {estacion}") """
