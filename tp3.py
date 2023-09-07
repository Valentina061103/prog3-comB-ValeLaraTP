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
odd_numbers=0 
for e in range(postitive_num+1): 
    if e%2!=0 : 
        odd_numbers+=1
        print(f" La cantidad de numeros impares es :  {odd_numbers}") 

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

#11 Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
word = str(input("ingrese una palabra: "))
word2 = word[::-1]


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