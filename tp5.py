#1
import tp5funciones
num_dni = (input("Ingrese su numero DNI: "))
if tp5funciones.dni(num_dni) == True:
    print("numero de dni valido")
else:
    print("numero de dni invalido")

#2
chain = input("Ingrese una cadena de texto: ")
tp5funciones.last_word_length(chain)
result = tp5funciones.last_word_length(chain) 
print("La longitud de la última palabra es:", result)

#3
name = input("ingrese su nombre comple con un solo apellido: ")
tp5funciones.name_member(name)
tp5funciones.long_last_name(name)
dni = input("ingrese su numero de dni: ")
tp5funciones.valid_dni(dni)
firt_name = tp5funciones.name_member(name)
long_last_name = tp5funciones.long_last_name(name)
last_three = tp5funciones.valid_dni(dni)
print("Nombre: ", name, "DNI: ", dni, "ID-> ",firt_name,long_last_name,last_three )

#4
number1 = int(input("Ingrese el primer número entero: "))
number2 = int(input("Ingrese el segundo número entero: "))
# Verificar si uno de los números es múltiplo del otro
if tp5funciones.es_multiplo(number1, number2):
    print(f"{number1} es múltiplo de {number2}")
elif tp5funciones.es_multiplo(number2, number1):
    print(f"{number2} es múltiplo de {number1}")
else:
    print("Ninguno de los números es múltiplo del otro.")

#5
num_days = int(input("Ingrese el número de días: "))
for day in range(1,num_days + 1):
    temp_max = float(input(f"Ingrese la temperatura máxima del día {day}: "))
    temp_min = float(input(f"Ingrese la temperatura mínima del día {day}: "))
    # Calcular la temperatura media 
    temp_media = tp5funciones.temperatura_media(temp_max, temp_min)
    # Mostrar la temperatura media
    print(f"La temperatura media del día {day} es: {temp_media:.2f} grados Celsius") #"{temp_media:.2f}" es para redondear a dos decimales

#6
text = input("Ingrese un texto: ")
resultado = tp5funciones.add_space(text)
print("Texto con espacios adicionales:")
print(resultado)

#7
valores = []
num_valores = int(input("Ingrese la cantidad de valores numéricos: "))
for i in range(num_valores):
    valor = float(input(f"Ingrese el valor {i + 1}: "))
    valores.append(valor)

maximo, minimo = tp5funciones.find_min_max(valores)
if maximo is not None and minimo is not None:
    print(f"El valor máximo es: {maximo}")
    print(f"El valor mínimo es: {minimo}")
else:
    print("No se ingresaron valores numéricos.")

#8
radio = int(input("Ingrese el radio del circulo: "))
area, perimetro = tp5funciones.peri_area_circulo(radio)
print(f"El area es {area}\nEl perimetro es {perimetro}")

#9
try_valid = 3
while try_valid>0:
    name_user = input("Ingrese el nombre de usuario: ")
    pasword = input("Ingrese la contaseña: ")

    user_valid = tp5funciones.valid_user(name_user, pasword)
    if user_valid:
        print("Datos correcto, ingreso valido")
        break
    else:
        print("Acceso denegado, los datos ingresados no son correctos")
        try_valid-=1

#10
#11
ele_list = ["palabra", "agua", "mar", "fumar"]
result = tp5funciones.aplicar_funcion(tp5funciones.add_space, ele_list)
print(result)

#12
frase = "Esta es una frase de ejemplo"
dictionary_length = tp5funciones.length_words(frase)
print(dictionary_length)

#13
vector_2d = [3, 4]  # Vector bidimensional (3, 4)
modulo_2d = tp5funciones.vector_modulus(vector_2d)
print(f"Módulo del vector 2D: {modulo_2d}")

#14
number = int(input("Ingrese un número para saber si es o no primo: "))
if tp5funciones.prime_number(number):
    print("Es primo")
else:
    print("No es primo")

#15
entered_numbers = 0
while True:
    try:
        number = int(input("Ingrese un número para conocer su factorial(-1 para salir): "))
        if number ==-1:
            break
        else:
            entered_numbers +=1
            factorial = tp5funciones.calcular_factorial(number)
            print(f"El factorial de {number} es {factorial}")
    except ValueError:
        print("El valor ingresado no es valido!")
print(f"Cantidad de números leidos: {entered_numbers}")

#16
try:
    number = int(input("Ingresa el número: "))
    digit = input("El digito que hay que buscar: ")
        
    if not digit.isdigit():
        print("Ingresa un dígito valido.")
    
    occurrences = tp5funciones.count_digit_occurrences(number, digit)
    print(f"El digito {digit} aparece {occurrences} en el número {number}.")
except ValueError:
    print("El número ingresado no es valido ")

#17
list_prime_numbers = []

while True:
    number = int(input("Número primo:"))
    if tp5funciones.prime_number(number):
        list_prime_numbers.append(number)
        get_add_digits =tp5funciones.add_digits(number)
        print(f"La suma de sus digitos es: {get_add_digits}")
        digit = int(input("Ingrese un dígito, para saber cuantas veces aparece: "))
        occurrences =tp5funciones.count_digit_occurrences(number, digit)
        print(f"El digito {digit} aparece {occurrences} en el número {number}")
    else:
        print("Termido de ingresar números primos, el número ingresado no lo es..")
        break

if list_prime_numbers:
    max_prime = max(list_prime_numbers)
    factorial_max = tp5funciones.calcular_factorial(max_prime)
    print(f"El mayor número ingresado es {max_prime} y su factorial es {factorial_max}")
else:
    print("No se ingresaron números.")