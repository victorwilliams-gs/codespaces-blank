#Suma de numeros pares

suma = 0
for i in range(50):
    numero = i + 1
    if numero % 2 == 0:
        suma += numero
print(f"La suma de los numeros pares entre 1 y 50 es: {suma}")