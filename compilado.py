#1) Conversion de metros a centimetros
metros = float(input("Introduce la longitud en metros: "))
centimetros = int(metros * 100)
print(f"La longitud en centimetros es: {centimetros} cm")



#2) Edad en el futuro
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
print(f"Hola {nombre}, en 10 años tendrás {edad + 10} años.")



#3) Area de un rectangulo
base = int(input("Base: "))
altura = int(input("Altura: "))
print(f"El área del rectangulo es: {base * altura}")



#4) Calculadora simple
n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multi}")
print(f"División: {int(div)}")



#5) Calculo del IVA
precio = float(input("Introduce el precio del producto: "))
iva = (precio * 0.19)
print(f"El precio final con IVA es: ${int(precio + iva)}")




#6) Promedio de tres numeros
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es {promedio:.2f}")



#7) Tiempo en segundos
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
resultado = horas * 3600 + minutos * 60 + segundos
print(f"El tiempo total es: {resultado} segundos")