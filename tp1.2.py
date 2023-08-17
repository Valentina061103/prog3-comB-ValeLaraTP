'''Trabajo Practico 1.2'''
#Ejercicio 1
base = float(input("ingrese el valor de la base del rectangulo "))
altura = float(input("ingrese el valor de la altura del rectangulo "))

area_rectangulo = base*altura
perim_rectangulo = (base*2)+(altura*2)

print(f'el area del rectangulo es:{area_rectangulo}.\nEl perimetro del rectangulo es: {perim_rectangulo}')

#ejercicio 2
cateto1 =  float(input("ingrese el valor del primer cateto: "))
cateto2 = float(input("ingrese el valor del segundo cateto: "))

hipotenusa = ((cateto1)**2 + (cateto2)**2)**(1/2)

print(f'la hipotenusa del triangulo es: {hipotenusa}')

