""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.  """

""" cont = 1

while cont < 101:
    print(cont)
    cont += 1 """

""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene.  """

""" num = int(input("Ingrese un numero: "))

cant_num = len(str(num))

print("El numero ingresado tiene", cant_num, "cifras") """

""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.  """

""" num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese un segundo numero: "))
sum = 0

for i in range(num_1+1,num_2):
    sum = sum + i
print("La suma de los numeros intermedios entre", num_1, "y", num_2, "es: ", sum) """

""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. """

""" num = int(input("Ingrese los numeros que desea sumar (Ingrese 0 para finalizar!): "))
sum = 0
if num > 0:
    while num != 0:
        sum = sum + num
        num = int(input("Ingrese los numeros que desea sumar (Ingrese 0 para finalizar!): "))
    print("Ha finalizado el ingreso de numeros, la sumatoria total es de ", sum)

elif num == 0:
    print("Ha finalizado el proceso, no hay ingreso de datos.") """

""" 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.  """

""" import random 

numeros_aleatorios = random.randint(1, 10)
num_usuario= int(input("Trate de adivinar un numero de 1 a 10 !: "))
total = 1

if num_usuario  != numeros_aleatorios:
    while num_usuario  !=  numeros_aleatorios:
        total += 1
        num_usuario= int(input("Intente otra vez! (de 1 a 10 !): "))
    print("Despues de ", total, "intentos, acerto! Felicidades!!")

elif  num_usuario  == numeros_aleatorios :
    print("Felicitaciones lo adivino a la primera!") """

""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. """

""" for i in range(100,0,-2):
    print(i-2) """

""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario.  """

""" num = int(input("Ingrese un numero: "))
sum = 0

for i in range(1,num):
    sum = sum + i
print("La suma total entre el numero ingresado ", num , "y cero es", sum) """

""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio).  """

""" par = 0
impar = 0
neg = 0
pos = 0

for i in range(1,101):
    num = int(input("Ingrese un numero entero ("+ str(i) +"/ 5 ): "))
    if num % 2 == 0:
        par += 1
    if num % 2 != 0:
        impar += 1
    if num < 0:
        neg += 1
    if num > 0:
        pos += 1
print("De los numeros ingresados la cantidades son las siguientes: ")
print("Pares : ", par)
print("Imares : ", impar)
print("Negativos : ", neg)
print("Positivos : ", pos) """

""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).  """

""" sum = 0

for i in range(1, 101):
    num = int(input("Ingrese un numero entero ("+ str(i) + " / 100 )"))
    sum += num
print("La media de los numeros ingresados es:", sum/5) """

""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. """


""" numero = input("Ingresa un número: ")

numero_invertido = numero[::-1]

print("El número invertido es:", numero_invertido) """
