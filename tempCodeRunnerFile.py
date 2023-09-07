divider = 0
while True:
    num = int(input("Ingrese un número positivo, para indicar si es o no primo: "))
    if num<=0:
        break
    for i in range(num):
        if num%(i+1) == 0 :
            divider += 1
    if divider == 2:
        print("Es un número primo")
    else:
        print("No es primo")