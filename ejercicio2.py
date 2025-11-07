while True:

    edad = int(input("Ingresa la edad del cliente: "))

    if edad < 0:
        print("Error de edad, por favor ingrese una edad correcta")
        continue

    if edad < 5:
        total = "Entrada gratis"
            
    elif 5 <= edad <= 11:
        total = "$5.000"
            
    elif 12 <= edad <= 59:
        total = "$8.000"
    
    elif edad >= 60:
        total = "$4.000"
    
    print(f"El precio a pagar de la entrada es: {total}")
    break


