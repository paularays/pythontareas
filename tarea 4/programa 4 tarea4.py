#Programa 4

dia=int(input("ingrese su dia de cumpleaños en numero entero"))
mes=int(input("ingrese su mes de cumpleaños del 1-12"))

if (dia >= 20) and (mes == 1) or (dia <= 18) and (mes == 2):
   print("acuario")

if (dia >= 19) and (mes == 2) or (dia <= 20) and (mes == 3):
   print("piscis")

if (dia >= 21) and (mes == 3) or (dia <= 19) and (mes == 4):
   print("aries")

if (dia >= 20) and (mes == 4) or (dia <= 20) and (mes == 5):
   print("tauro")

if (dia >= 21) and (mes == 5) or (dia <= 20) and (mes == 6):
   print("geminis")

if (dia >= 21) and (mes == 6) or (dia <= 22) and (mes == 7):
   print("cancer")

if (dia >= 23) and (mes == 7) or (dia <= 22) and (mes == 8):
   print("leo")

if (dia >= 23) and (mes == 8) or (dia <= 22) and (mes == 9):
   print("virgo")

if (dia >= 23) and (mes == 9) or (dia <= 22) and (mes == 10):
   print("libra")

if (dia >= 23) and (mes == 10) or (dia <= 21) and (mes == 11):
   print("escorpio")

if (dia >= 22) and (mes == 11) or (dia <= 21) and (mes == 12):
   print("sagitario")
            
if (dia >= 22) and (mes == 12) or (dia <= 19) and (mes == 1):
   print("capricornio")




print("fin")


