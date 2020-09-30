class Docente:

    def registrar_docente(self):
        cant_docente = int(input("Ingrese cantidad de docentes a registrar: "))
        docentes = []
        try:
            for i in range(cant_docente):
                while True:
                    try:
                        print("Ingrese sus datos")
                        print("========================")
                        print(f"\nDocente N°{i+1}")
                        nombre = input("Ingrese su nombre: ")
                        dni = int(input("Ingrese su dni: "))
                        edad = int(input("Ingrese su edad: "))

                        datos_docente = {
                            'Id': i,
                            'Nombre': nombre,
                            'DNI': dni,
                            'Edad': edad
                        }

                        docentes.append(datos_docente)
                        break
                    except ValueError:
                        print(f"Has ingresado un valor erroneo en los datos del docente N°{i+1}")
            file = open("docentes.txt", 'a', encoding='UTF-8')
            for f in docentes:
                linea = f"Nombre: {f['Nombre']}, DNI:{f['DNI']}, Edad: {f['Edad']}\n"
                file.write(linea)
        finally:
            file.close()
    
    def registrar_alumno(self):
        cant_alumnos = int(input("Ingrese cantidad de alumnos a registrar: "))
        lista_alumnos = []
        lista_calificaciones = []

        try:
            for a in range(cant_alumnos):
                while True:
                    try:
                        print("Ingrese sus datos")
                        print("======================")
                        print(f"\n Alumno N°{a+1}")
                        nombre = input("Ingrese su nombre: ")
                        
                        cant_notas = int(input("Ingrese cantidad de notas a registrar: "))

                        for n in range(cant_notas):
                            while True:
                                try:
                                
                                    notas = float(input(f"Ingrese Nota N°{n+1}: "))

                                    if notas >= 0 and notas <=20:
                                        lista_calificaciones.append(notas)
                                        break
                                    else:
                                        if notas < 0:
                                            print("Solo puede ingresar calificacion de 0 a 20, Intente nuevamente...")
                                        else:
                                            print("No puede ingresar calificaciones superior a 20, Intente nuevamente...")
                                            
                                except ValueError:
                                    print("Solo puede digitar numeros, Intente nuevamente...")

                        datos_alumno = {
                            'Nombre': nombre,
                            'Nota Maxima': max(lista_calificaciones),
                            'Nota Minima': min(lista_calificaciones),
                            'Promedio': sum(lista_calificaciones)/len(lista_calificaciones)
                        }
                        lista_alumnos.append(datos_alumno) 
                        break
                    except Exception:
                        print("Ha ingresado un valor incorrecto, Intente nuevamente...")
            
            file = open("alumnos.txt", 'a', encoding='UTF-8')
            for i in lista_alumnos:
                linea = f"Nombre: {i['Nombre']}, Nota Maxima: {i['Nota Maxima']}, Nota Minima: {i['Nota Minima']}, Promedio: {i['Promedio']}\n"
                file.write(linea)
        finally:
            file.close()
