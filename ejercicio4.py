print("Bienvenido a Heladeria Frosty \n Sabores y precios: \n chocolate → $4.000 \n vainilla → $3.500")

precios = {"chocolate":4000, "vainilla":3500}

while True:
    sabor = input("Escribe el sabor de helado que quieras: ").lower()

    if sabor in precios:
        total = precios[sabor]
        topping = input("Quieres adicionar un topping? Valor $1.000. si/no: ")
        if topping == "si":
            total += 1000
        
        print(f"El valor a pagar es {total}")
        break

    else:
        print("El sabor escrito no existe, por favor ingresa uno correcto")

