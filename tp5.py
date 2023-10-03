def dni (num_dni):
    if len(num_dni) == 7 or len(num_dni) == 8:
        return True
    else:
        return False

num_dni = (input("Ingrese su numero DNI: "))
if dni(num_dni) == True:
    print("numero de dni valido")
else:
    print("numero de dni invalido")
