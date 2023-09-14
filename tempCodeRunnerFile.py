digitos_pares = 0
digitos_impares = 0
out = input("Bienvenido para ingresar empezar ingrese 1: ")
while out != 0:
    num = int(input("ingrese los numeros que quiere analizar: "))
    if num % 2 == 0:
        print(f"{num} es par")
        digitos_pares += 1
    elif num % 2 != 0:
        print(f"{num} es impar")
        digitos_impares += 1
        out = input("desea agregar otro numero? Presione 1 para 'SI' y 0 para 'NO': ")
    if out == 0:
        break