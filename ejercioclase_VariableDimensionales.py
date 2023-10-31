#1
# Inicializar las listas de pasajeros y ciudades
pasajeros = []
ciudades = []

# Función para agregar un pasajero a la lista de viajeros
def agregar_pasajero():
    nombre = input("Nombre del pasajero: ")
    dni = int(input("DNI del pasajero: "))
    destino = input("Destino del pasajero: ")
    pasajeros.append((nombre, dni, destino))
    print("Pasajero agregado correctamente.")

# Función para agregar una ciudad a la lista de ciudades
def agregar_ciudad():
    ciudad = input("Nombre de la ciudad: ")
    pais = input("País de la ciudad: ")
    ciudades.append((ciudad, pais))
    print("Ciudad agregada correctamente.")

# Función para buscar el destino de un pasajero por su DNI
def buscar_destino_por_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for nombre, pasajero_dni, destino in pasajeros:
        if pasajero_dni == dni:
            print(f"{nombre} viaja a {destino}.")
            return
    print("No se encontró ningún pasajero con ese DNI.")

# Función para contar cuántos pasajeros viajan a una ciudad dada
def contar_pasajeros_por_ciudad():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    count = sum(1 for _, _, destino in pasajeros if destino == ciudad)
    print(f"La cantidad de pasajeros que viajan a {ciudad} es {count}.")

# Función para buscar el país de destino de un pasajero por su DNI
def buscar_pais_por_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for _, pasajero_dni, destino in pasajeros:
        if pasajero_dni == dni:
            for ciudad, pais in ciudades:
                if ciudad == destino:
                    print(f"{dni} viaja a {pais}.")
                    return
    print("No se encontró ningún pasajero con ese DNI.")

# Función para contar cuántos pasajeros viajan a un país dado
def contar_pasajeros_por_pais():
    pais = input("Ingrese el nombre del país: ")
    count = sum(1 for _, destino_pais in ciudades if destino_pais == pais)
    print(f"La cantidad de pasajeros que viajan a {pais} es {count}.")

# Menú iterativo
while True:
    print("\nMenu:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Ver destino de pasajero por DNI")
    print("4. Contar pasajeros por ciudad")
    print("5. Ver país de destino de pasajero por DNI")
    print("6. Contar pasajeros por país")
    print("7. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        agregar_pasajero()
    elif opcion == "2":
        agregar_ciudad()
    elif opcion == "3":
        buscar_destino_por_dni()
    elif opcion == "4":
        contar_pasajeros_por_ciudad()
    elif opcion == "5":
        buscar_pais_por_dni()
    elif opcion == "6":
        contar_pasajeros_por_pais()
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
