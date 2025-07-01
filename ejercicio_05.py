# Un sistema digital restringido solicita al usuario ingresar un nombre de usuario y una
# contraseña. Si ambos coinciden exactamente con los valores esperados ('admin' y '1234'), se
# debe mostrar 'Acceso concedido'. En caso contrario, mostrar 'Acceso denegado'. Crea el
# algoritmo para esta validación.

usuario= input("Ingrese su usurio: ")
contraseña= int(input("ingrese contraseña: "))
if usuario == "admin" and contraseña == "1234" :
    print("Acceso concedido")
else:
    print("Acceso denegado")    

