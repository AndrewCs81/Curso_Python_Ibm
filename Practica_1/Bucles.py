"""


1-Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:

- Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).
numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1
Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
i = 0
while i < len(lista_numeros) :
    if lista_numeros[i]>0:
        print(lista_numeros[i])
        i += 1
    else:
        break    
1-Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista.
mi_lista = list(range(2500,2586))
print(mi_lista)


2-lista con multiplos de 3
mi_lista = list(range(3,300,3))
print(mi_lista)


3-recorre la lista y suma los cuadrados de los elementos
mi_lista = list(range(1,16))
suma_cuadrados = 0
for i in mi_lista:
    suma_cuadrados += i**2
print(suma_cuadrados)            
"""



"""
1- Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for nombre in alumnos_clase :
    print(f"Hola {nombre}!")

2- Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for i in lista_numeros :
    suma_numeros = suma_numeros + i
    print (suma_numeros)
    
3- Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:

  lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]  
suma_pares = 0
suma_impares = 0

for i in lista_numeros :
    if i % 2 == 0 :
        suma_pares = suma_pares + i
        print(f"par={i},Acumulado ={suma_pares}")
    else:
        suma_impares = suma_impares + i
        print(f"impar={i},Acumulado ={suma_impares}")
"""


