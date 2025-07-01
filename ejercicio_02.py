# Un centro de salud recibe temperaturas tomadas de los pacientes al ingresar. Se debe
# desarrollar un algoritmo que reciba como entrada una temperatura (en grados Celsius) y
# muestre un mensaje indicando si el paciente presenta: - Hipotermia (menos de 36°C) - Temperatura normal (entre 36°C y 37.5°C inclusive) - Fiebre (más de 37.5°C)

temp = float(input("ingrese su temperatura: "))
if temp < 36 :
    print("El paciente presenta hipotermia.")
elif temp >= 36 and temp <= 37.5 :
    print("El paciente presenta temperatura normal.")
elif temp > 37.5 :
    print("El paciente presenta fiebre.")

 