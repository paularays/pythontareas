#Programa 2
Tiempo=int(input("introduce el tiempo en segundos:"))

horas=Tiempo//3600
modulo=Tiempo%3600
minutos=modulo//60
modulo=modulo%60
segundos=modulo

print("horas;",horas)
print("minutos;",minutos)
print("segundos;",segundos)
print("fin")
