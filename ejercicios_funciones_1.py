#DEFINICION DE FUNCIONES
def most(a,b):
    if (a>b):
        return a
    else:
        return b
def least(a,b):
    if (a<b):
        return a
    else:
        return b
#PROGRAMA PRINCIPAL
a = int(input("un numero: "))
b = int(input("otro numero: "))
print(most(a-3, least(a+2, b-5 )))