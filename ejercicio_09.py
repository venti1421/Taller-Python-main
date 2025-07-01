# Una empresa de energía desea categorizar a sus clientes en tres rangos tarifarios según el
# consumo mensual de kilovatios-hora (kWh): - Menor a 100 kWh → 'Estrato bajo' - Entre 100 y 200 kWh → 'Estrato medio' - Mayor a 200 kWh → 'Estrato alto'
# Desarrolla un algoritmo que reciba el consumo y muestre la categoría correspondiente. 


consumo = int(input("ingrese su consumo en kwh: "))
if consumo < 100 :
    print("El cliente es estrato bajo.")
elif consumo >=100 and consumo <=200 :
    print("el cliente es estrato medio.")
elif consumo > 200 :
    print("el clinte es estrato alto.")
