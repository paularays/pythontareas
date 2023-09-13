#Programa 3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

mayor = a

if (b > mayor):
    mayor = b
if (c > mayor):
    mayor = c


print(f"El número mayor es: {mayor}")

print("fin de program")

