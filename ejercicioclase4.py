fecha = input("dia, DD/MM: ")
dia_sem = fecha[0:fecha.find(",")]
dia = fecha[fecha.find(" ")+1:fecha.find("/")]
mes = fecha[fecha.find("/")+1:]
dia_sem = dia_sem.lower()

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
            if dia_sem == "lunes" or dia_sem == "martes" or dia_sem == "miercoles":
                nivel_inicial = str(input("¿Hubo examen? "))
            if nivel_inicial == "si":
                aprob_n_i = int(input("ingrese cantidad de aprobados: "))
                desaprob_n_i = int(input("ingrese cantidad de desaprobados: "))
                aprobados = (aprob_n_i/(aprob_n_i + desaprob_n_i))*100
                print("El porcentaje de alumnos aprobados es: %",aprobados)
