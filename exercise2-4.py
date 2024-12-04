# Calculo del promedio y evaluacion

nota = input("Ingrese nota: (fin para detener)")

suma_notas = 0
cantidad_notas = 0      
while nota != "fin":
    nota = float(nota)
    suma_notas += nota
    cantidad_notas += 1
    nota = input("Ingrese nota: (fin para detener)")

promedio = suma_notas / cantidad_notas
print(f"El promedio es: {promedio}")
if promedio >= 4.0:
    print("¡Aprobaste!")
else:
    print("Reprobaste")




