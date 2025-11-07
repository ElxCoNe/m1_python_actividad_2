libro = 25000

print("Bienvenido a la liberia El saber \n Tenemos descuento para estudiantes y además un cupón para ellos \n El valor del libro es $25.000")

estudiante = input("Eres estudiante? si/no: ").lower()
if estudiante == "si":
    total = libro * 0.85
    cupon = input("Por favor ingresa el cupón de descuento: ").upper()
    if cupon == "LIBRO10":
        total = total * 0.90

    print(f"Total a pagar {total:,.0f}")
else:
    print(f"Total a pagador ${libro:,.0f}")

