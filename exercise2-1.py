#Generar una lista de numeros
n = int(input("n = "))
counter = 1
lista = []
while counter <= n:
    lista.append(counter)
    counter += 1

print(lista)