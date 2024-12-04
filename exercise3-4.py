#Juego de adivinanza

target = 8
numero = int(input("Adivine un numero entre el 1 y 20: "))

while target != numero:
    if numero < target:
        print("El numero es menor")
    elif numero > target:
        print("El numero es mayor")
    numero = int(input("Adivine un numero entre el 1 y 20: "))

print("Acertaste!")
