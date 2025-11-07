producto_costo = 2000

cantidad = int(input("Ingrese las cantidades que desees comprar: "))

costo = cantidad * producto_costo 



if cantidad >= 30:
    costo_desc = costo * 0.85
elif cantidad >= 10:
    costo_desc = costo * 0.95
else:
    costo_desc = costo


if costo_desc < 50000:
    costo_desc += 5000

print(f"Total a pagar {costo_desc:,.0f}")

