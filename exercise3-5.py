#Tabla de multiplicar

numero = int(input("Ingrese un numero entero: "))

for i in range(10):
    operando = i + 1
    producto = numero * operando
    print(f"{numero} x {operando} = {producto}")

    