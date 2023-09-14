#1
x = int(0)
while x <30 :
    x = x+1
    if x== 15:
        print("The execution of the loop was broken when x was " , x)
        break
    if (x==4) or (x==6) or (x==10):
        print('The value ', x ,' of x was skipped')
        continue
    print('The value of the loop is: ', x)

#1
while True:
    text = input("Ingrese texto para imprimirlo en mayusculas: ")
    if text:
        print(text.upper())
    else:
        break
#2
action="d"
cantidad=0
total=0
salida=True
while salida==True:
    action=input("ingrese 'd' y la cantidad a depositar o 'r' y la cantidad a retirar:  ")
    action.lower
    if(action==""):
        break
    elif (action[0]=="d"):
        #desde el número siguiente al espacio, y como no sabemos cuantos digitos tiene, indicamos su final con len()
        cantidad=int(action[action.find("")+1: len(action)])
        total+=cantidad
    elif(action[0]=="r"):
        cantidad=int(action[action.find(" "): len(action)])
        total-=cantidad
    else:
        print("no es posible realizar esta operacion")
print("El total en su cuenta es de: ", total)

#3
#Utilizo una funcion para indicar si es primo
def es_primo(number):
    if number <2:
        return False
    for i in range(2, number):
        if number% i == 0:
            return False
    return True

prime_numbers = 0
number = int(input("Ingrese números mayores que 1 (o 0 para terminar): "))
while number!=0:
    if es_primo(number):
        prime_numbers+=1
    number = int(input("Ingrese otro número: "))
print("La cantidad de números primos ingresados es: ", prime_numbers)

#4
def bisiesto(anio):
    if (anio%4==0 and anio%100!=0) or (anio%400==0):
        return True
    return False

print("A continuación ingrese 2 años, para indicar en ese rango cuales son bisiestos, multiplos de 10")
year1 = int(input("Ingrese el primer año: "))
year2 = int(input("Ingrese en segundo año: "))
for y in range(year1, year2+1,1):
    if bisiesto(y) and y%10==0:
        print(y, " es un año bisiesto y multiplo de 10")

#5
print("Números impares del 1 al 20: ")
for n in range(1, 21):
    if n%2 !=0:
        continue
    print(n)

#6
number_list =[1,2,3,4,5,6,7,8,9,10]
find_number = int(input("Ingrese que número quiere buscar: "))
for n in number_list:
    if n == find_number:
        print("Número encontrado ", n)
        break

#7
while True:
    print("Menú de opciones:")
    print("1. azul")
    print("2. rojo")
    print("3. Amarillo")
    print("0. Salir")
    option = input("Seleccione una opción: ")

    if option == "1":
        print("Ha elegido azul")
    elif option == "2":
        print("Ha elegido rojo")
    elif option == "3":
        print("Ha elegido amarillo")
    elif option == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")