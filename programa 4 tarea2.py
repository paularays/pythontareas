#Prgrama 4
numero=float(input("cual es el numero?"))
decimales=int(input("cuantos decimales?"))

cantidad= 10 ** decimales
redondear=int(numero * cantidad + 0.5)/cantidad


print(redondear)

print("final")
