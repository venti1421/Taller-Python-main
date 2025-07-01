#  Múltiplos de 3 y 5 – Clasificación numérica múltiple
# Un sistema numérico automatizado necesita clasificar números según su divisibilidad por 3,
# por 5, o por ambos. Escribe un algoritmo que reciba un número entero y muestre en
# pantalla uno de los siguientes mensajes: - “Es múltiplo de 3 y 5” - “Es múltiplo solo de 3” - 
# “Es múltiplo solo de 5” - “No es múltiplo de 3 ni de 5”

num = int(input("ingrese un numero: "))
if (num % 3 == 0 and num % 5 == 0 ):
    print(f"El numero {num} es multiplo de 5 y 3 ")
elif (num % 3 == 0):
    print(f"El numero {num} es multiplo de 3 ")
elif (num % 5 == 0):
    print(f"El numero {num} es multiplo de 5 ")
else:
    print(f"El numero {num} no es multiplo de 5 y 3")    



