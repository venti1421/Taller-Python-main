# Un sistema de reservas permite elegir entre 3 tipos de evento:
# 1. Cine ($20.000)
# 2. Teatro ($35.000)
# 3. Concierto ($50.000)
# Luego debe ingresar la cantidad de entradas deseadas. Si el total supera los $100.000, se
# aplica un 10% de descuento. Calcula el total a pagar.

print("seleccione el tipo de evento: ")
print("1. Cine $20.000")
print("2. Teatro $35.000")
print("3. Concierto $50.000")
evento = int(input("Ingrese el número del tipo de evento: "))   
entradas = int(input("Ingrese la cantidad de entradas: "))
match evento:
    case 1:
        costo = entradas * 20000
    case 2:
        costo = entradas * 35000
    case 3:
        costo = entradas * 50000
if costo > 100000:
    descuento = costo * 0.10
    total = costo - descuento
    print(f"Se aplica descuento del 10% total a pagar es:{total} ")
else :
    print(f"total a pagar es: {costo}")


