#Filtrar numeros pares

texto = input("Ingrese los numeros separados por un espacio: ")

lista = texto.split()
pares = []
for item in lista:
    numero = int(item)
    if numero % 2 == 0:
        pares.append(numero)

print(pares)