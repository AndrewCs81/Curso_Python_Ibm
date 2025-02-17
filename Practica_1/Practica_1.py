
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