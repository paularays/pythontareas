#programa 6
tornillo=int(input("ingresa el numero del tornillo"))
columna=tornillo//8
renglon=tornillo%8

x=(renglon * 15)+7.5
y=(columna * 15)+ 7.5

print("se encuentra en el renglon;",renglon)
print("se encunetra en la columna;",columna)
print("coordenada x:",x)
print("coordenada y:",y)
print("fin")
