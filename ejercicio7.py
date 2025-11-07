print("Bienvenido al sabor colombianos \n Menu tiene costo de $12.000 con opcion de bebida ")


menu = 12000
opcion_bebidas = {"si": 3000, "no": 0}

opcion = input("desea agregar la bebida? Tiene un costo de $3.000 (si/no): ").lower()

if opcion in opcion_bebidas:
    valor_bebida = opcion_bebidas[opcion]
else:
    print("opción invalida, se asumira que no desea bebida.")
    valor_bebida = 0

total = (menu + valor_bebida) * 1.08 

print(f"Total a pagar es: ${total:,.0f}")


