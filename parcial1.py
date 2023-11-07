odd_number = 0 #declaracion de variables
sum_odd_num = 0
average_odd_num = 0
bigest_even_num = 0
vowel_a = 0
vowel_e = 0
vowel_i = 0
vowel_o = 0
vowel_u = 0
name_user = input("Bienvenido/a, ingrese su nombre para iniciar: ")
option = int(input(f"Hola, {name_user} para jugar a: \nJugegos de numeros -> ingrese 1 \nJuego de palabras -> ingrese 2\n:")) #se le pide al usurio la opction
if option == 1:  #condicion para entrar juego uno
    print(f"Bienvenido/a {name_user} al juego de numeros, deberas ingresar numeros enteros y para salir ingrese 0: \n ")
    while True: #entra bucle
        number = int(input(f"{name_user} , ingrese numero entero:\n "))
        if number == 0: #condicion de salida
            break
        if number % 2 != 0:  #numeros pares
            odd_number += 1 #contador para nuemros
            sum_odd_num += number  #se suma los numeros y se los guarda en la varible sum_odd_num
        else:
            if number % 2 == 0: #numeros impares
                if number > bigest_even_num: #se guarda el numero mas grande, 
                    bigest_even_num = number #si el numero es mas grande del que estaba anteriormente guardado, se remplaza en la variable bigest_even_num
    if odd_number > 0:
            average_odd_num = sum_odd_num / odd_number #saco promeio impares
            print(f"{name_user} el promedio de los numeros impares es: {average_odd_num}") #muestro
    else:
            print(f"{name_user} no se ingresaron numeros impares") #en caso que no se hayan ingresado
    if bigest_even_num != 0:
            print(f"{name_user}, el mayor numero par es: {bigest_even_num}") #muestro mayor numero
    else:
            print(f"{name_user} no se ingresaron numeros pares") #en caso que no hayan ingresado
else:
    if option == 2: #condicion entrada juego 2
        print(f"Bienvenido/a {name_user} al juego de palabras, deberas ingresa una frase: \n")
        phrase = (input(f"{name_user}, ingrese la frase: ")).lower() #se pide la frase y se la pasa a minusculas para evaluarla
        for letra in phrase: #variable letra recorre toda la frase y si se encuentra la vocal se suma en el contador correspondiente
            if letra == "a":
                vowel_a += 1
            if letra == "e":
                vowel_e += 1
            if  letra == "i":
                vowel_i += 1
            if letra == "o":
                vowel_o += 1
            if letra == "u":
                vowel_u += 1
    print(f"{name_user}, la cantidad de \nA: {vowel_a}\nE: {vowel_e}\nI: {vowel_i}\nO: {vowel_o}\nU: {vowel_u}") #muestra cantidades
