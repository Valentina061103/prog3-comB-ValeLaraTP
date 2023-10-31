import random

# Lista de palabras para adivinar
palabras = ["python", "tecnologia", "programacion", "computadora", "inteligencia", "datos", "algoritmo"]

def seleccionar_palabra():
    return random.choice(palabras)

def jugar():
    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos_restantes = 6  # Número de intentos permitidos

    print("¡Bienvenido al juego del ahorcado!")
    palabra_oculta = "_" * len(palabra)

    while True:
        print(f"Palabra: {palabra_oculta}")
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra.")
        elif letra in palabra:
            letras_adivinadas.append(letra)
            palabra_oculta = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

            if palabra_oculta == palabra:
                print(f"Felicidades, adivinaste la palabra: {palabra}!")
                break
        else:
            letras_adivinadas.append(letra)
            intentos_restantes -= 1
            print(f"Letra incorrecta, te quedan {intentos_restantes} intentos.")

            if intentos_restantes == 0:
                print(f"Perdiste. La palabra era: {palabra}")
                break

if __name__ == "__main__":
    jugar()
