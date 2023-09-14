# Ejer 1 
word=input("Ingrese una palabra y se le mostrara 10 veces : ") 
for i in range(5): 
    print(word)

#2 ​Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). 
birthday_year =int(input(" Ingrese su edad : ")) 
for year in range(birthday_year+1) : 
    if year !=0 : 
        print(F"{year}")

#3 ​Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas. 
postitive_num= int(input("Ingrese un numero entero positivo : ")) 
odd_numbers= ""
for e in range(1,postitive_num+1,1): 
    if e%2!=0 : 
        odd_num = str(e)
        odd_numbers += odd_num
        odd_numbers += ","
        print(f" Los numeros numeros impares son :  {odd_numbers}") 

#4 ​Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. 
num= int(input("Ingrese un numero entero positivo : ")) 
k=1 
for k in range(num +1): 
    print(num-k,end=",") 
    print(" ") 

#5 ​Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.  
investment=int(input("Ingrese cuanto desea invertir ")) 
annual_interest= int(input(" Cual es el interes anual ?  ")) 
year=int(input("Ingrese cuantos años desea invertir ")) 
for y in range(year): 
    annual_earnings=(investment*annual_interest)/100 
    investment= investment + annual_earnings 
print( f" En el año { y+1 } el usuario gano un { annual_earnings}") 

#6 ​Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido. 
numero= int(input("Ingrese un numero para la altura de su triangulo: "))  
for i in range(numero+1): 
    print(" ") 
    for j in range(i): 
        print("*",end=" ") 
        print(" ") 

#7 Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}= {i*j}")

#8 Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo
n = int(input("introduce la altura del triangulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
        print(" ")

#9 Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta
password = "contraseña"
password2 = "u"

while (password != password2):
    password2  = input("ingrese la contraseña: ").lower()

#10 Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
divider = 0
while True:
    num = int(input("Ingrese un número positivo, para indicar si es o no primo, si desea sallir ingrese 0: "))
    if num<=0:
        break
    for i in range(num):
        if num%(i+1) == 0 :
            divider += 1
    if divider == 2:
        print("Es un número primo")
    else:
        print("No es primo")

#11 Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
word = str(input("ingrese una palabra: "))
word2 = word[::-1]
print(f"la palabra invertida sera: {word2}")

#12 Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
phrase = str(input("ingrese una frase: "))
letter = input("ingrese la letra que quiera buscra: ")
count = phrase.count(letter)
print(f"la letra elegida se repite {count} de veces en la frase escrita")

#13 Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminar
word_13 = " "
while word_13 != "salir":
    word_13 = str((input("escriba algo: "))).lower()
    echo = word_13
    print(f"eco: {echo}")

#14 Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo
number=int(input("Ingrese un numero: "))
number_2=int(input("Ingrese otro numero: "))
print(f"Vamos a ver si los numeros que se encuentran entre {number} y {number_2} son pares o impares: ")
for i in range(number,number_2+1):
    if i %2==0:
        print(f"Numero par: {i}")
    else:
        print(f"Numero impar: {i}")

#15 Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores
while True:
    num = int(input("Escriba el numero del cual quiere conocer sus divisores: "))
    if num <= 0:
        break
    for i in range(num):
        divider = 0
        if num%(i+1) == 0:
            divider +=1
            print("los divisores de ",num, "son ", i+1 )

#16 Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
amount = int(input("indique cuantos numeros va ingresar: "))
negative = 0
for i in range(amount):
    num = int(input("ingrese el numero: "))
    if num < 0:
        negative +=1
print("se han introducido: ", negative, " numeros negativos")

#17 Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas)
phrase = (input("ingrese una frase: ")).lower()
vowel = "aeiou"
for i in vowel:
    if i in phrase: 
            print(i)

#18 ​Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
#La sucesión comienza con los números 0 y 1 y, a partir de éstos, 
#cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55… 
before1 = 0
before2 = 1
sequence = "0 1 "
for i in range(9) :
    new = before1 +before2
    before1 = before2
    before2 = new
    num3 = str(new)
    sequence += num3
    sequence += " "
print(sequence)

#19 Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar.
# A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. 
# El programa deberá comprobar que las cantidades ingresadas sean positivas
objetive=int(input("ingrese la cantidad de dinero que desa ahorrar: "))
save=0
while (save<=objetive):
    money=int(input("Cuanto vas a ingresar?"))
    if (money>=0):
        save+=money
        print(save)
    else:
        print("no se pueden ingresar numeros negativos")
        print("objetivo alcanzado")

#20 Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresado
addition=0
num=1
while (num!=0):
    num=int(input("ingrese un numero distinto de 0: "))
    addition+=num
print("la sumatoria de los numeros ingresados es: ", addition)

#21 Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado
number=1
max=0
while (number!=0):
    number=int(input("ingrese un numero distirnto a 0: "))
    if(number>max):
        max=number
print("El mayor numero ingresado es: ", max)

#22 Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
#La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
number=0
addition=0
addition_2=0
while(number!=-1):
    number=int(input("Ingrese un numero, para salir ingrese '-1': "))
    if (number>=0):
        for n in str(number):
            n=int(n)
            addition+=n
        print(addition)
    else:
        print("el numero ingresado debe ser positivo")
    if (number % 2==0):
        addition_2+=1
    print("la cantidad de numeros ingresados pares son: ", addition_2)

#23 ​Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el monto 0. 
amount_enter = 1
while amount_enter != 0:
    amount_enter = float(input("ingrese el monto de la compra para terminar ingrese 0:  "))
    if amount_enter == 0:
        print("Termino de cargar los montos")

#24 Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
#Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
# se le debe aplicar un 10% de descuento. 
print("ingrese los montos para calcular el total de su compra: ")
total_amount = 0
amount = 0
out = 0
while out !=1:
    amount = float(input("ingrese el monto: "))
    out = int(input("Para agregar otro monto ingrese '0' y para terminar ingrese '1': "))
    if amount < 0:
        print("monto invalido. Por favor ingrese nuevamente: ")
        continue
    total_amount += amount 
if total_amount > 1000:
    total_amount_discount = (total_amount - ((total_amount*10)/100))
    print("el total a pagar es de: $", str(total_amount_discount), "con el descuento de %10 por la compra de mas de $1000")
else:
    total_amount = total_amount
    print("el total a pagar es de: $", total_amount)

#25 ​Dado un número entero positivo, mostrar su factorial. 
#El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. 
#El factorial de 0 es 1. 
while True:
    number = int(input("ingrese un numero entero para factorizar: ")) #si ve estos antes que la vea, le hago una consulta
    if number < 0:                                                    #como puedo evitar que el usuario ingrese un numero con coma?
        print("por favor ingrese un numero positivo")                 #porque en el if de la linea 233 quiese poner 'if number == float' se imprimera el mensaje
    else:                                                             #pero no funciono
        if number == 0:
            print("el factorial de 0 es 1")                
        continue                                                 
    for i in range(number):
        factor = number * i
        print( number, " x ", i, " = ", factor)
    out = input("Si quiere ingresar otro numero para factorear ingrese 'm' y si quiere salir ingrese 's': ")
    out_low = out.lower()
    if out_low == "m":
        print("gracias por seguir con nosotros")
    else:
        print("gracias, vuelva pronto")
        break
