#Clasificador de edades

clasificar = True

while clasificar:
    cantidad = int(input("¿Cuantas edades desea clasificar?: "))

    edades = {}

    while cantidad > 0:
        print()
        edad = int(input("Ingresa una edad: "))
        if edad < 13:
            categoria = "Niño"
        elif edad >= 13 and edad < 18:
            categoria = "Adolescente"
        elif edad > 17 and edad < 60:
            categoria = "Adulto"
        elif edad >= 60:
            categoria = "Adulto mayor"
    
        if categoria not in edades:
            edades[categoria] = 0
        edades[categoria] += 1
        print(f"Categoria: {categoria}")
        cantidad -= 1

    print()
    print("Resumen")
    for category in edades:
        label = f"{category}s"
        if category == "Adulto mayor":
            label = "Adultos mayores"
        print(f"{label} : {edades[category]}")

    print()
    option = input("¿Quieres clasificar más edades? (si/salir): ")
    if option == "salir":
        clasificar = False