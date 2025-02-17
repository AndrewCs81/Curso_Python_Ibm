palabra = 'ordenador'
resultado = palabra[1]  # Obtiene la segunda letra de la palabra ('r')
#print(resultado)

palabro = 'las carchofas no estaban en la paella'
resultados = palabro.index('paella')  # Encuentra la posición donde comienza 'paella'
#print(resultados)

palabros = 'las carchofas no estaban en la paella, pero me compre unas gambas y las meti en otra paella'
resultados = palabros.rindex('paella')  # Encuentra la última aparición de 'paella'
#print(resultados)

frase = 'controlar la complejidad es la esencia de la programacion'
resultado = frase[0:9]  # Extrae los primeros 9 caracteres ('controlar')
#print(resultado)
resultado = frase[9::3]  # Toma cada tercer carácter a partir del índice 9
#print(resultado)

frase = 'es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza'
resultado = frase[::-1]  # Invierte la frase completamente
print(resultado)

# Diccionario con valores variados
dic = {'c1': 10, 'c2': ['a', 'b', 'c'], 'c3': {'x1': 100, 'x2': 'andrew'}}
print(dic['c3']['x2'].upper())  # Accede a 'x2' dentro del diccionario anidado y lo convierte en mayúsculas
print(dic.items())  # Devuelve los elementos clave-valor del diccionario
print(dic.values())  # Devuelve solo los valores
print(dic.keys())  # Devuelve solo las claves

# Otro diccionario con datos personales
mi_dic = {'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': 35, 'ocupacion': 'Periodista'}
print(mi_dic)  # Imprime el diccionario completo

# Diccionario anidado con listas y valores
mi_dict = {"valores_1": {"v1": 3, "v2": 6}, "puntos": {"points1": 9, "points2": [10, 300, 15]}}
print(mi_dict["puntos"]['points2'][1])  # Accede al segundo valor de la lista dentro de 'points2'

# Agregar un nuevo par clave-valor al diccionario
mi_dic["pais"] = 'colombia'
print(mi_dic)

# Tupla con valores repetidos
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))  # Cuenta cuántas veces aparece el número 2 en la tupla
mi_tupla = list(mi_tupla)  # Convierte la tupla en lista para poder modificarla
print(type(mi_tupla))  # Verifica el nuevo tipo de la variable

# Conjuntos (sets) y operaciones
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_2.union(mi_set_1)  # Une ambos conjuntos sin repetir elementos
print(mi_set_3)

# Operaciones con conjuntos
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
resultado = sorteo.pop()  # Elimina y devuelve un elemento aleatorio del conjunto
print(resultado)

sorteo.add('Damian')  # Agrega un nuevo elemento al conjunto
print(sorteo)
