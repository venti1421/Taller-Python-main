# Diseña un algoritmo que reciba un número del 1 al 7 y muestre el día correspondiente de la
# semana. Si se ingresa un número fuera de ese rango, mostrar un mensaje de error. Usa una
# estructura ‘según’ o ‘switch’.
num = int(input("ingrese un numero del 1-7 para validar dia de la semana: "))
if num >= 1 and num <= 7 :
    match num:
        case 1:
            print(" El dia 1 corresponde a Lunes.")
        case 2:
            print(" El dia 2 corresponde a Martes.")
        case 3:
            print(" El dia 3 corresponde a Miercoles.")
        case 4:
            print(" El dia 4 corresponde a Jueves")
        case 5:
            print(" El dia 5 corresponde a Viernes.")
        case 6:
            print(" El dia 6 corresponde a Sabado.")
        case 7:
            print(" El dia 7 corresponde a Domingo.")
else:
    print("Error numero fuera del rango")
