#15 15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores
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
for i in phrase:
    if i in vowel: 
            print(i)