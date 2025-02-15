

Texto   = input("Dame un texto para analizar: ")
Tocapelotas = 0

while True:
  Letra_1 = input( " Ahora dame una letra: ")
  if Letra_1.isalpha() and len(Letra_1) == 1:
    print("Letra correcta, puedes continuar")
    break
  elif Tocapelotas == 3:
    print("te voy a romper el pc ya!")
    break

  else:
    print ("No me tomes el pelo y mete una letra,solo UNA letra!")
    Tocapelotas = Tocapelotas+1


 

while True:
  Letra_2 = input( " Ahora dame la segunda letra, pero no juegues conmigo eh: ")
  if Letra_2.isalpha() and len(Letra_2) == 1:
    print("Letra correcta, puedes continuar")
    break
  elif Tocapelotas == 3:
    print("voy a quemarte la casa joder")
    break
  else:
    print ("Te dije que no juegues conigo,pon una letra ya")
    Tocapelotas = Tocapelotas+1


while True:
  Letra_3 = input( " Ahora dame la tercera letra y tengamos la fiesta en paz eh: ")
  if Letra_3.isalpha() and len(Letra_3) == 1:
    print("Letra correcta, puedes continuar")
    break
  elif Tocapelotas == 3:
    print("Voy a matar a tu perro y follarle el culo")
    break
  else:
    print ("Pon una puta letraaaaaaaaa!!!!")
    Tocapelotas = Tocapelotas+1