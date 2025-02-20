
Texto = input("Dame un texto para analizar: ")
Tocapelotas = 0

while True:
    Letra_1 = input("Ahora dame una letra (y no me hagas enfadar...): ")
    if Letra_1.isalpha() and len(Letra_1) == 1:
        print("¡Bien! Una elección sabia.")
        break
    elif Tocapelotas == 3:
        print("Las luces parpadearán... y tu PC hará ruidos extraños... ¡elige bien! 😈")
        break
    else:
        print("Mmm... Eso no es una letra. ¿Sabes lo que es una letra? 🤨")
        Tocapelotas += 1

while True:
    Letra_2 = input("Dame otra letra. Pero ojo... te estoy vigilando. 👀: ")
    if Letra_2.isalpha() and len(Letra_2) == 1:
        print("Bien, bien... Vas por buen camino.")
        break
    elif Tocapelotas == 3:
        print("Acabas de desbloquear el nivel experto de sustos. 🎃")
        break
    else:
        print("¿En serio? ¿Otra vez? Mira que hay consecuencias... ⏳")
        Tocapelotas += 1

while True:
    Letra_3 = input("Última letra... Elige con sabiduría, o podrías despertar algo... 😨: ")
    if Letra_3.isalpha() and len(Letra_3) == 1:
        print("¡Perfecto! Has sobrevivido... por ahora. 😏")
        break
    elif Tocapelotas == 3:
        print("Se oyen golpes en la puerta... demasiado tarde. 💀")
        break
    else:
        print("Última oportunidad antes de que el teclado empiece a moverse solo... 👻")
        Tocapelotas += 1


# Sacando el numero de repeticiones de letras

MiniTexto = Texto.lower()

Repite_L1 = MiniTexto.count(Letra_1)
print(f"Tu primera letra '{Letra_1}' se repite :{Repite_L1} veces")

Repite_L2 = MiniTexto.count(Letra_2)
print(f"Tu segunda letra '{Letra_2}' se repite :{Repite_L2} veces")

Repite_L3 = MiniTexto.count(Letra_3)
print(f"Tu tercera letra '{Letra_3}'se repite :{Repite_L3} veces")


## Sacando el numero de palabras

palabras = MiniTexto.split() # Divide el texto en una lista de palabras
Cpalabras = len(palabras)
print(f"El texto elegido tiene : {Cpalabras} palabras")

## Busco la primera y ultima palabra 

print(f"La primera palabra es '{palabras[0]}' y la ultima es '{palabras[-1]}'")

## Busco las palabras mas repetidas

conteo  = {}
for palabra in palabras:
    if palabra in conteo :
        conteo[palabra] += 1 # Si la palabra ya está, sumamos 1
    else :
        conteo[palabra] = 1 # Si no está, la iniciamos en 1

for palabra, cantidad in conteo.items():
    if cantidad > 3:
        print(palabra, cantidad)       





"""verificar su contenido:
a través de las palabras clave
in
y
not in
. Elresultado de esta verificación es un booleano (
True
/
False
)."""