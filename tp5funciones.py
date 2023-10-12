#1
def dni (num_dni):
    if len(num_dni) == 7 or len(num_dni) == 8:
        return True
    else:
        return False

#2
def last_word_length(chain):
    words = chain.strip().split()
    if words:
        last_word = words[-1]
        return len(last_word)
    else:
        return 0
    
#3
def name_member(name):
    firts_name = name.strip().split()
    firts_name = firts_name[0]
    return firts_name

def long_last_name(name):
    last_name = name.strip().split()
    last_name = last_name[-1]
    long = len(last_name)
    return long


def valid_dni(dni):
    if len(dni) == 7 or len(dni) == 8:
        last_three_dni = dni[-3:]
    else:
        print("numero dni invalido, vuelva ingresar: ")
    return last_three_dni

#4 
def es_multiplo(numero, multiplo_de):
    return numero % multiplo_de == 0

#5
def temperatura_media(temp_maxima, temp_minima):
    return (temp_maxima + temp_minima) / 2

#6
def add_space(texto):
    text_with_space= " ".join(texto)
    return text_with_space

#7
def find_min_max(values):
    if len(values) == 0:
        return None, None  # Si la lista está vacía, no hay máximo ni mínimo
    maximo = values[0]
    minimo = values[0]
    for value in values:
        if value > maximo:
            maximo = value
        elif value < minimo:
            minimo = value
    return maximo, minimo

#8
import math
def peri_area_circulo(radio):
    area =  math.pi* (radio**2)
    perimetro = (radio*2)* math.pi
    return area, perimetro

#9
def valid_user(nombre, password):
    if nombre == "usuario1" and password == "asdasd":
        respuesta = True
    else:
        respuesta = False
    
    return respuesta

#10
#11
def aplicar_funcion(funcion, list):
    nueva_lista = []
    for element in list:
        result = funcion(element)
        nueva_lista.append(element)
    return result

#12
def length_words(frase):
    # Dividir la frase en palabras
    words = frase.split()

    result = {}
    for word in words:
        length= len(word)
        result[word] = length
    return result

#13
def vector_modulus(vector):
    if len(vector) == 2:  # Two-dimensional vector
        x, y = vector
        modulus = math.sqrt(x**2 + y**2)
    elif len(vector) == 3:  # Three-dimensional vector
        x, y, z = vector
        modulus = math.sqrt(x**2 + y**2 + z**2)
    else:
        raise ValueError("The vector must be two-dimensional or three-dimensional.")
    
    return modulus

#14
def prime_number(number):
    divisor =0
    for n in range(1,number+1):
        if number%n == 0:
            divisor+=1
    if divisor ==2:
        return True
    else:
        return False

#15
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

#16
def count_digit_occurrences(number, digit):
    number = str(number)
    count = 0
    for d in number:
        if d == digit:
            count += 1
    return count

#17
def add_digits(number):
    add = 0
    for d in str(number):
        add += int(d)
    return add

