""" 1 - Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal. 
def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo() """

""" ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// """

""" 2 -  Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. 
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario. 
def saludar_usuario():
    print(f"Hola {name}, mucho gusto!") 

name = input("Ingrese su nombre: ")
saludar_usuario() """

""" ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// """

""" 3 - Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados. 

def informacion_personal():
    age = int(input("Ingrese su edad: "))
    name = input("Ingrese su nombre: ")
    lname = input("Ingrese su apellido: ")
    res = input("Ingrese su residencia: ")

    print(f"“Soy {name} {lname}, tengo {age} años y vivo en {res}”.") 

informacion_personal() """

""" ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// """

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados. 

from math import pi

def calcular_area_circulo(radio):
    a = pi * radio * radio
    print(f"El are del radio ingresado es {a}")

def calcular_perimetro_circulo(radio):
    p = 2 * pi * radio
    print(f"El perimetro del radio ingresado es {p}") 

radio = int(input("Ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio) """

""" ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// """

""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"Los segundos ingresados equivaldran a {horas} hora/s") 

segundos = int(input("Ingrese los segundos a convertir: "))
segundos_a_horas(segundos) """

""" ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// """

""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(num):
    for i in range(1,11):
        multi = num * i
        print(f"{num} x {i} = {multi}")

num = int(input("Ingrese un numero del cual quiera saber su tabla de multiplcar: "))
tabla_multiplicar(num) """

""" ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// """


""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara. 

def operaciones_basicas(a, b):
    sum = num1 + num2
    res = num1 - num2
    multi = num1 * num2
    div = num1 / num2
    print(f"Se aplico las operaciones aritmeticas basicas a los numeros {num1} y {num2}:  \nSuma : {num1} + {num2} = {sum}\nResta : {num1} - {num2} = {res}\nMultiplicacion : {num1} * {num2} = {multi}\nDivision : {num1} / {num2} = {div} ")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

operaciones_basicas(num1, num2) """

""" ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// """


""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales. 

def calcular_imc(a, b):
    imc = a / (b * b)
    return print(f"Sun IMC es de {imc:.1f}")


alt = float(input("Para saber su indice de masa corporal, primero ingrese su altuma (en metros): ")) 
peso = float(input("Ingrese su peso: "))

calcular_imc(peso, alt) """

""" ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// """

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función. 

def celsius_a_fahrenheit(celsius):
    f = c * (9 / 5) + 32
    print(f"{c}° en Celsius equivale a {f}° Fahrenheit")

c = float(input("Ingrese una temperatura en grados celsius: "))
celsius_a_fahrenheit(c) """

""" ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// """

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta función. """

""" def calcular_promedio(a, b, c):
    sum = num1 + num2 + num3
    prom = sum / 3
    print(f"El promedio de los tres numeros ingresados es: {prom}")


num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

calcular_promedio(num1, num2, num3) """