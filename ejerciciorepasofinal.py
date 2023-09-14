total_price = 0 #iniciando varibles
dicount = 0.10
product_list = []
exit = True
position = 0

while exit == True:
    option = input("Para agregar sus productos a lista ingrese 1, de lo contrario ingrese 2: ")
    if (option =="1"):
        product_list.append(input("Que producto desea agregar?")) #guradamos en el array los productos
    elif (option == "2"):
        break
    else:
        print("la opcion ingresada no corresponde a ninguna de las solicitadas")
        continue
for i in product_list:
    find_product = int(input("Encontraste el producto en el supermercado? Ingrese 1 para 'si' y 2 para 'no': "))
    if (find_product != 1 or find_product != 2):
        while (find_product != 1 or find_product !=2):
            find_product = input("la opcion ingresada no es valida, ingrese la opcion nuevamente: ")
    elif (find_product == 1):
        product_price = float(input("que precio tenia el producto?: "))
        total_price += product_price
    else:
        replace_product = int(input("Desea remplazar el producto? 1 para 'si' y 2 para 'no': "))
        if replace_product == 1:
            product_list[position] = input("Por cual producto desea remplazarlo?: ")
            product_price = float(input("Que precio tenia el producto?: "))
            total_price += product_price
        else:
            continue
        position += 1
tipe_of_pay = int(input("Si dea pagar en efectivo ingrese 1, sino ingrese 2"))
if tipe_of_pay != 1 and tipe_of_pay != 2:
    tipe_of_pay = input("la opcion no es valida, ingrese nuevamente: ")
elif tipe_of_pay == 1:
    total_price = total_price*0.10
print("el total a pagar es: ", total_price)
