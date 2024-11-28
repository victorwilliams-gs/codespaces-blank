#Tiempo en segundos
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

resultado = horas * 3600 + minutos * 60 + segundos

print(f"El tiempo total es: {resultado} segundos")