# Desarrolla un algoritmo que muestre un menú con las siguientes opciones:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# El usuario elige una opción e ingresa dos números. El programa debe realizar la operación
# seleccionada y mostrar el resultado. Si la división es por cero, indicar 'No se puede dividir
# por cero'. 
print("Elija en del siguiente menu que opcion de operación desea ralizar: ")
print("1. Sumar.")
print("2. Restar.")
print("3. Multiplicar.")
print("4. Dividir.") 
operacion = int(input("Elija opcion: "))
num_1 = float(input("ingrese el primer numero: "))
num_2 = float(input("ingrese el segundo numero: "))
if operacion >=1 and operacion <=4 :
    match operacion :
        case 1 :
            print("el resultdo de la suma es: ", num_1 + num_2 )
        case 2 :
            print("El resultado de la resta es: ", num_1 - num_2 )
        case 3 :
            print("el resultdo de la multiplicacion es: ", num_1 * num_2 )
        case 4 :
            if num_2 == 0 :
                print("no se puede dividir por cero.")
            else :
                print("El resultado de la resta es: ", num_1 / num_2 )
else:
    print("Opcion no valida")



