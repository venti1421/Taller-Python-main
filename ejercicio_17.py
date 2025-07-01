# Crea un programa que lea un número del 1 al 12 y muestre el nombre del mes
# correspondiente. Por ejemplo, 1 → 'Enero', 2 → 'Febrero', etc. Si se ingresa un número
# inválido, mostrar 'Mes no válido'. 
mes = int(input("ingrese un numero del 1-12 para validar el mes correspondiente: "))
if mes >= 1 and  mes <= 12 :
    match mes :
        case 1 :
            print("Es el mes de Enero.")
        case 2 :
            print("Es el mes de Febrero,")
        case 3 :
            print("El se mes de marzo")
        case 4 :
            print("Es el mes de Abril.")
        case 5 :
            print("Es el mes de Mayo.")
        case 6 :
            print("El se mes de Junio")
        case 7 :
            print("Es el mes de Julio.")
        case 8 :
            print("Es el mes de Agosto.")
        case 9 :
            print("El se mes de Septiembre")
        case 10 :
            print("Es el mes de Octubre.")
        case 11 :
            print("Es el mes de Noviembre,")
        case 12 :
            print("El se mes de Diciembre")
else :
    print("Mes no valido.")

