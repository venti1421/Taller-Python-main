# Dependiendo del tipo de actividad, se aplica una retención: - Dependiente → 10% - Independiente → 15% - Empresario → 20%
# Solicita el tipo y el ingreso mensual y calcula el valor del impuesto. Valida que los ingresos
# sean positivos.

print("ingrese el tipo de actividad: ")
print("1. Dependiente")
print("2. Independiente")
print("3. Empresario")
tipo = int(input("Ingrese el número del tipo de actividad: "))
ingreso = float(input("Ingrese el ingreso mensual: "))
if ingreso < 0:
    print("El ingreso debe ser positivo.")
else:
    match tipo:
        case 1:
            impuesto = ingreso * 0.10
            print(f"El impuesto a pagar para un dependiente es: {impuesto}")
        case 2:
            impuesto = ingreso * 0.15
            print(f"El impuesto a pagar para un independiente es: {impuesto}")
        case 3:
            impuesto = ingreso * 0.20
            print(f"El impuesto a pagar para un empresario es: {impuesto}")
        