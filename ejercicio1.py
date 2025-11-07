precio_unidad = 300

while True:


    panes = int(input("Ingresa la cantidad de panes que desea comprar: "))
    

    if panes < 0:
        print("Cantidad invalida")
        continue
    
    total_sin_desc = panes * precio_unidad

    
    if panes <= 20:
        print(f"Debido a que son menos de 20 panes la compra, el total a pagar es: ${total_sin_desc}")
            
    elif 20 < panes <= 50:
        total_con_desc = total_sin_desc * 0.90
        print(f"Por la compra de mas de 20 panes, el total a pagar con el 10% de descuento es: ${total_con_desc}")
            
    elif panes > 50:
        total_con_desc = total_sin_desc * 0.80
        print(f"Por la compra de mas de 50 panes, el total a pagar con el 20% de descuento es: ${total_con_desc}")
        
    break









