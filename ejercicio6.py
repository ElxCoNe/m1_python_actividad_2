while True:
    horas = int(input("Por favor ingresar cuantas horas permanecio en el parqueadero: "))

    if horas <= 0:
        print("Horas invalidas, por favor seleccionar un número de horas correcto")
        continue

    elif 0 < horas <= 5:
        total = horas * 2000
        break
    
    else:
        total = (horas * 2000) + 5000 
        break

print(f"Total a pagar de parqueadero: ${total:,.0f}")




