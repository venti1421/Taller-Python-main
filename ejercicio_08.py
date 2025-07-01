# Una institución educativa aprueba a un estudiante si cumple dos condiciones: una nota final
# igual o superior a 3.0 y una asistencia igual o superior al 80%. Escribe un algoritmo que
# reciba estos dos datos y determine si el estudiante aprueba o reprueba.

nota_final = float(input("ingrese nota final: "))
asistencia = int(input("ingrese el porcentaje de asistencia: "))
if nota_final >= 3 and asistencia >= 80 :
    print("El estudiante aprueba: ")
else :
    print("El estudiante reprueba")

