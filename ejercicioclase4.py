#Ejercicio 1
corrimiento=int(input("Ingrese la cantidad de espacios que se correran las letras: "))
alfabeto="abcdefghijklmnñopqrstuvwxyz"

for i  in range(5):
    mensaje=input("Mensaje a encriptar: ").lower()
    mensaje_encriptado=''
    for letra in mensaje:
        if letra in alfabeto:
            indice=alfabeto.find(letra)
            indice=(indice+corrimiento)%27
            mensaje_encriptado+=alfabeto[indice]
        else: 
            mensaje_encriptado+=letra 
    print(f'El mensaje encriptado es: {mensaje_encriptado}')

#Ejercicio 2
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