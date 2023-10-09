#juego dados

import random

#entrada del casino
credito=int(input("¿cuanto es tu credito?"))

#mesa de apuesta
seguirJugando=True
while seguirJugando:

    sumaApuesta=-1#para forzar while
    while sumaApuesta<2 or sumaApuesta>12:
          sumaApuesta=int(input("suma a la apuesta?"))

          if sumaApuesta<2 or sumaApuesta>12:
              print("Miserable usuario, el numero debe ser entre 2 y 12")
    
    montoApuesta=0
    while montoApuesta<=0 or montoApuesta>credito:
          montoApuesta=float(input("Monto de la apuesta?"))

    dado1=random.randint(1,6)
    dado2=random.randint(1,6)

    sumaDados=dado1+dado2

    print("dados",dado1,dado2)
    print("suma:",sumaDados)

    if(sumaApuesta==sumaDados):
        print("ganaste")
        credito+=montoApuesta

    else:
        print("por favor intenta nuevamente(perdiste)")
        credito-=montoApuesta

    print("tu credito es:$%9.2f"%(credito))


#revisar si quire seguir jugando
    if credito<=0:
       print("Ya no tienes dinero. ¡Hasta la proxima!")
       seguirJugando=False

    else:
       respuesta=input("Desea seguir jugando? [s/n]")
    if respuesta.lower()=="n":
        seguirJugando=False
        print("Gracias por jugar. ¡Hasta la proxima!")

print("fin del programa")





