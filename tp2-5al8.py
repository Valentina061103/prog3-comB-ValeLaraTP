#5
letra = (input("ingrese una letra: ")).lower()
if letra == "a" or letra == "e" or letra == "i" or letra == "i" or letra =="o" or letra == "u":
    print("la letra ", letra, " es una vocal")
else:
    print("la letra ", letra, " es una consonante")
if len(letra)> 1:
    print("error, solo puede ingresar una letra")

#6
año = int(input("ingrese el año que quiere analizar: "))
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print("año bisiesto")
else:
    print("año no bisiesto")

#7
num1 = int(input("ingrese numero 1: "))
num2 = int(input("ingrese numero 2: "))
num3 = int(input("ingrese numero 3: "))
if num1 < num2 and num1 < num3:
    print(num1, " es el menor")
elif num2 < num1 and num2 < num3:
    print(num2, " es el menor")
else:
    if num3 < num1 and num3 < num2:
        print(num3, " es el menor")

#8
usuario = str(input("ingrese usuario: "))
contraseña = str(input("ingrese contraseña"))
if usuario == "Gwenevere" and contraseña == "excalibur":
    print("usuario y contraseña correctps. Puede ingresar a Camelort")
else:
    print("acceso denegado")

#19
cantidad_lapices = int(input("ingrese cantidad de lapices a comprar"))
precio = 60
if cantidad_lapices >= 1000:
    sin_descuento = precio*cantidad_lapices
    descuento = (sin_descuento*7)/100
    precio_final = sin_descuento - descuento
    print("Por la compra de ", cantidad_lapices, "tiene un 7 porciento de descuento, su nuevo total es de: ", precio_final)
else:
    sin_descuento = precio*cantidad_lapices
    print("Por la compra de ", cantidad_lapices, "usted no tiene acceso a un descuento, su total es: ", sin_descuento)


