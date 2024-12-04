#Sumar elementos de una lista

lista = input("Ingrese numeros separados por espacios: ")

lista = lista.split()

suma = 0

for item in lista:
    numero = int(item)
    suma += numero

print(f"La suma de los elementos es: {suma}")
