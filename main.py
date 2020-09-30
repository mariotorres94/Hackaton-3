#Crea un programa que permita registrar docentes y alumnos con su nombre, dni y edad. Dichos datos deberán registrarse
# en un archivo de texto llamado.txt y docentes.txt respectivamente
# En el caso de los alumnos, se podrán ingresar hasta 4 notas, las mismas que serán promediadas y serán mostradas en un
# archivo de texto como reporte.
# Dicha información contendra el siguiente formato:
# nro: <1>
# - Alumno: <nombre alumno>, maxima nota: <nota máxima>, minima nota: <nota minima>, promedio: <nota promedio>
# - Para el docente su reporte será:
# Docente: <Nombre docente>, Edad: <edad>, DNI: <Su dni>

import objetos

print("\n\t .:: Bienvenido ::.\n")
print("\t Que desea realizar")
print("""
    \t1) Registrar Docente
    \t2) Registrar Alumno
    \t3) Salir
""")

opcion = input("\tSeleccione una opcion: ")

docente = objetos.Docente()

if opcion == '1':
    docente.registrar_docente()
elif opcion == '2':
    docente.registrar_alumno()
else:
    exit()
    