# 1. Solicita al usuario que ingrese 25 números únicos, uno a la vez, para completar su cartón de bingo. Los
# números deben estar en el rango de 1 a 75.
# 2. Valida que los números ingresados sean únicos y estén dentro del rango permitido. Si el usuario ingresa un
# número duplicado o fuera del rango, debe mostrar un mensaje de error y solicitar otro número.
print("Bienvenido al Bingo")
print("Para empezar, debes completar los números de tu cartón.")
print("Los números deben ser positivos del 1 al 75 sin repetir.")

array_bingo = []
repet = 0

while len(array_bingo) < 25:
    numero = int(input("Ingresa un número: "))
    if numero < 1 or numero > 75:
        print("Por favor, ingresa un número entre 1 y 75.")
    elif numero in array_bingo:
        print("Número repetido. Por favor, ingresa otro número.")
    else:
        array_bingo.append(numero)
print("Tu cartón de Bingo ha sido completado:")
print(array_bingo)

row = 5
column = 5
pos= 0
bingo_card = [[0 for i in range(row)] for j in range(column)]
for i in range(row):
    for j in range(column):
        bingo_card[i][j] = array_bingo[pos]
        pos +=1
print(bingo_card)

# 3. Después de que el usuario haya completado su cartón, inicia el juego de Bingo.
# 4. Extrae bolas de bingo al azar y verifica si los números extraídos están en el cartón del usuario.
# 5. Continúa extrayendo bolas de bingo hasta que el jugador complete una línea horizontal, vertical o diagonal
# en su cartón


