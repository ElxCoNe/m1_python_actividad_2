edad = int(input("Ingrese su edad: "))
documento = input("tiene documento si/no: ").lower()

if edad < 18:
    print("entrada denegada")
else:
    if documento == "si":
        print("Puede entrar")
    else:
        print("Debe presentar documento")

