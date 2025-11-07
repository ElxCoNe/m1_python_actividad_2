print("Bienvenido a Solo Leveling Fit")
print("Selecciona cuantos días entrenaste esta semana")
print("1. ≥ 4 días")
print("2. 2 o 3 días")
print("3. 0 o 1 días")

puntos = 0

while True:
    opcion = int(input("Ingresa la Op: "))

    match opcion:
        case 1:
            puntos+=1
            print(f"¡Excelente disciplina, has ganado {puntos} punto de energia!")
            
        
        case 2:
            print("Bien, pero puedes dar más")

        case 3:
            print("No aflojes, tú puedes mejorar")

        case _:
            print("Opción no existente, por favor ingresar una correcta")

    break