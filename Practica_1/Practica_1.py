

Texto   = input("Dame un texto para analizar: ")


while True:
  Letra_1 = input( " Ahora dame una letra: ")
  if Letra_1.isalpha() and len(Letra_1) == 1:
    print("Letra correcta, puedes continuar")
    break
  else:
    print ("No me tomes el pelo y mete una letra,solo UNA letra!")
