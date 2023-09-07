fecha = input("dia, DD/MM: ")
dia_sem = fecha[0:fecha.find(",")]
dia = fecha[fecha.find(" ")+1:fecha.find("/")]
mes = fecha[fecha.find("/")+1:]
dia_sem = dia_sem.lower()
nivel_inicial = 0

if dia_sem != "lunes" and dia_sem != "martes" and dia_sem != "miercoles" and dia_sem != "jueves" and dia_sem != "viernes":
    print("error, dia no valido")
else:
    if dia > "31":
        print("error, numero de dia no valido")
    else:
        if mes > "13":
            print("error,numero de mes no valido")
        else:
            print(fecha)
if dia_sem == "lunes":
    nivel_inicial = str(input("¿Hubo examen? "))
    if nivel_inicial == "si":
        aprob_n_i = int(input("ingrese cantidad de aprobados: "))
        desaprob_n_i = int(input("ingrese cantidad de desaprobados: "))
        aprobados = (aprob_n_i/(aprob_n_i + desaprob_n_i))*100
        print("El porcentaje de alumnos aprobados nivel inicial es: %",aprobados)
if dia_sem == "martes":
    nivel_intermedio = str(input("hubo examen? "))
    if nivel_intermedio == "si":
        aprobado_n_int = int(input("ingrese cantidad de aprobados: "))
        desaprobado_n_int = int(input("ingrese cantidad de desaprobados: "))
        aprobados_int = (aprobado_n_int/(aprobado_n_int + desaprobado_n_int))*100
        print("el porcentaje de alumnos aprobados del nivel intermedio es: %", aprobados_int) 
if dia_sem == "miercoles":
    nivel_avanzado = str(input("hubo examen? "))
    if nivel_avanzado == "si":
        aprobado_n_a = int(input("ingrese cantidad de aprobados: "))
        desprobado_n_a = int(input("ingrese cantidad de desaprobados: "))
        aprobados_a = (aprobado_n_a/(aprobado_n_a + desprobado_n_a))*100
        print("el porcentaje de alumnos aprobados en el nivel avanzado es de: %", aprobados_a)
if dia_sem == "jueves":
        asistencia = int(input("ingrese el porcentaje de asistencia: "))
        if asistencia > 50:
            print("asistio la mayoria")
        else:
            print("no asistio la mayoria")
if dia_sem == "viernes":
    if dia == "01" or mes == "07":
        print("inicio de nuevo ciclo")
        cant_alum_viaj = int(input("ingrese cantidad de alumnos: "))
        arancel = int(input("ingrese arancel por alumno: "))
        total_arancel = cant_alum_viaj * arancel
        print("el ingreso total del curso es de: $", total_arancel)