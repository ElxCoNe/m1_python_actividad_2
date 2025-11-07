while True:
    nota_tecnica = float(input("Por favor ingresa la nota de tu prueba técnica: "))
    nota_logica = float(input("Por favor ingresa la nota de tu prueba lógica: "))

    if 0.0 <= nota_tecnica <= 5.0 and 0.0 <= nota_logica <= 5.0:
        nota_final = (nota_tecnica * 0.7) + (nota_logica * 0.3)

        if nota_final >= 3:
            print("Felicidades aprobaste")
            break
        elif 2 <= nota_final < 3:
            print("Revision")
            break
        else:
            print("Reprobado")
            break
            
    else:
        print("Rango de notas es invalida, por favor escribirlas en el rago de 0.0 al 5.0")


   