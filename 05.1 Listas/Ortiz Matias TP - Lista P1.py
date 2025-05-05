""" 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 

lista = list(range(0,101,4))
print(f"{lista}") """

""" 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!  

gustos = ['programar', 'helado', 'misperros', 'migato', 'micasa']
print(f"{gustos[2]}") """

""" 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.
lista_vacia = []

lista_vacia.append('hola')
lista_vacia.append('como')
lista_vacia.append('estas?')

print(f"{lista_vacia}") """

""" 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.  Imprimir la lista resultante por pantalla. 
¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! 

animales = ["perro", "gato", "conejo", "pez"] 
print(f"{animales}")

animales[1]='loro'
animales[3]='oso' 
print(f"{animales}") """

""" 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.  

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#De las lista [numeros] proporcionada de 5 valores, se borra o quita con la funcion (max) el numero mas alto de la lista y por ultimo se imprimen los restantes """

""" 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros. 

lista = list(range(10,30,5))

print(f"{lista[0]}, {lista[1]}") """

""" 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
cualesquiera.  

autos = ["sedan", "polo", "suran", "gol"] 

autos[1]='Ferrari'
autos[2]='Renault'
print(f"{autos}") """

""" 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
directamente. Imprimir la lista resultante por pantalla.  

doble = []

doble.append(5)
doble.append(10)
doble.append(15)
print(f"{doble}") """

"""  9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

a) Agregar "jugo" a la lista del tercer cliente usando append. 
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
c) Eliminar "pan" de la lista del primer cliente.  
d) Imprimir la lista resultante por pantalla 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

compras[2].append('jugo')
compras[1][1] = 'tallarines'
compras[0].remove('pan')
print(f"{compras}") """

""" 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
● Posición lista_anidada[0]: 15 
● Posición lista_anidada[1]: True 
● Posición lista_anidada[2][0]: 25.5 
● Posición lista_anidada[2][1]: 57.9 
● Posición lista_anidada[2][2]: 30.6 
● Posición lista_anidada[3]: False 
Imprimir la lista resultante por pantalla. 

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]
print(f"{lista_anidada}") """