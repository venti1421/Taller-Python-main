﻿# Un proveedor de servicios de Internet desea implementar una herramienta que clasifique el
# servicio que tiene un usuario. Se debe ingresar la velocidad del plan en Mbps y mostrar:
# - 'Muy lenta' si es menor a 10 Mbps - 'Aceptable' si es entre 10 y 30 Mbps - 'Buena' si es entre 31 y 100 Mbps - 'Alta velocidad' si es mayor a 100 Mbps

velocidad = int(input("Ingrese la velocidad del plan en Mbps: "))
if velocidad < 10 :
    print("Muy lenta")
elif velocidad >= 10 and velocidad <= 30:
    print("Aceptable")
elif velocidad >= 31 and velocidad <= 100:
    print("Buena")
elif velocidad > 100:
    print("Alta velocidad")