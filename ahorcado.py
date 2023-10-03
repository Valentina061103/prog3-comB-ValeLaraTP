import random

def guess_word(word_selected, letter):
    word_find = ""
    for i in word_selected:
        if i == letter:
            word_find += letter
        else:
            word_find += "_"
    return word_find


user_attempts = 0
word_find = ""
word_list = ["computadoras", "python", "java", "softwere", "variables", "programacion"]
print("Bienvenido/a al juego del ahorcado")
print("La palabra es: ")
word_selected = random.choice(word_list)
spaces = len(word_selected)
amount_spaces = "_" * spaces
print(amount_spaces)
for i in range(12):
    letter = input("ingrese letra y descubra si esta en la palabra: ")
    print(guess_word(word_selected,letter))
    word_selected = word_find