# Un parqueadero cobra según el tipo de vehículo: - Carro → $5.000/hora - Moto → $2.000/hora - Bicicleta → $500/hora
# Diseña un algoritmo que reciba el tipo de vehículo y el número de horas y calcule el total a pagar.

print("Seleccione el tipo de vehículo:")    
print("1. Carro")
print("2. Moto")
print("3. Bicicleta")
tipo = int(input("Ingrese el número del tipo de vehículo: "))   
horas = int(input("Ingrese el número de horas: "))
match tipo:
    case 1:
        costo = horas * 5000
        print(f"El total a pagar por el carro es: {costo}")
    case 2:
        costo = horas * 2000
        print(f"El total a pagar por la moto es: {costo}")
    case 3:
        costo = horas * 500
        print(f"El total a pagar por la bicicleta es: {costo}")     