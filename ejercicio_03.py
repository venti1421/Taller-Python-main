# Para garantizar la seguridad, una montaña rusa permite el ingreso solo a personas que
# tengan una edad igual o mayor a 12 años y una estatura igual o mayor a 1.40 metros. Crea
# un algoritmo que reciba la edad y estatura de una persona y determine si puede subir o no a
# la atracción. 

edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su estatura en metros: "))
if edad >= 12 and altura >= 1.4 :
    print("Puede subir a la atracción.")
else :
    print("No puede subir a la atracción.")  
      