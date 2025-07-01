# En una tienda de tecnología se aplican descuentos por el valor total de la compra: - Sin descuento si es menor a $100.000 - 5% si está entre $100.000 y $200.000 - 10% si supera los $200.000
# Crea un algoritmo que reciba el valor de la compra y muestre qué porcentaje de descuento
# aplica. 

compra = int(input("Ingrese el valor de la compra: "))
if compra < 100000:
    print("Sin descuento.")
elif compra >= 100000 and compra <= 200000:
    print("Su descuento es de 5%.")
elif compra > 200000:
    print("Su descuento es de 10%.")