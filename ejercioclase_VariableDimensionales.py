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

#2
def obtener_domicilios_factura(ventas):
    domicilios_factura = set()  # Usamos un conjunto para evitar duplicados

    for venta in ventas:
        cliente, _, _, domicilio = venta  # Desempaquetamos la tupla
        domicilios_factura.add(domicilio)

    return list(domicilios_factura)  # Convertimos el conjunto a una lista

# Ejemplo de uso
ventas = [('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'), ('Jorge Russo', 7, 3999, 'Calle 2 - 741'),
        ('Nuria Costa', 12, 876.0, 'Calle 1 - 456')]  # Incluimos una venta adicional para 'Nuria Costa'
domicilios = obtener_domicilios_factura(ventas)
print(domicilios)

#3
# Inicialización de datos con los socios fundadores
socios = {
    1: {"nombre": "Amanda Núñez", "ingreso": "17/03/2009", "cuota_al_dia": True},
    2: {"nombre": "Bárbara Molina", "ingreso": "17/03/2009", "cuota_al_dia": True},
    3: {"nombre": "Lautaro Campos", "ingreso": "17/03/2009", "cuota_al_dia": True}
}

# Función para informar la cantidad de socios
def cantidad_socios():
    return len(socios)

# Función para registrar que un socio ha pagado todas las cuotas adeudadas
def pagar_cuotas(socio_numero):
    if socio_numero in socios:
        socios[socio_numero]["cuota_al_dia"] = True
        print(f"El socio {socio_numero} ha pagado todas las cuotas adeudadas.")
    else:
        print(f"No se encontró al socio con el número {socio_numero}.")

# Función para modificar la fecha de ingreso de los socios
def corregir_fecha_ingreso(fecha_original, fecha_corregida):
    for socio_numero, datos_socio in socios.items():
        if datos_socio["ingreso"] == fecha_original:
            datos_socio["ingreso"] = fecha_corregida

# Función para dar de baja a un socio
def dar_de_baja(nombre_apellido):
    for socio_numero, datos_socio in list(socios.items()):
        if datos_socio["nombre"] == nombre_apellido:
            del socios[socio_numero]
            print(f"El socio {nombre_apellido} ha sido dado de baja.")

# Función para imprimir el listado de socios completo
def imprimir_listado_socios():
    for socio_numero, datos_socio in socios.items():
        estado_cuota = "al día" if datos_socio["cuota_al_dia"] else "adeudada"
        print(f"Socio n°{socio_numero}: {datos_socio['nombre']}, ingresó el {datos_socio['ingreso']}, cuota {estado_cuota}.")

# Menú iterativo
while True:
    print("\nMenú:")
    print("1. Informar cantidad de socios")
    print("2. Registrar pago de cuotas")
    print("3. Corregir fecha de ingreso")
    print("4. Dar de baja a un socio")
    print("5. Imprimir listado de socios")
    print("6. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        print(f"La cantidad de socios es: {cantidad_socios()}")
    elif opcion == "2":
        socio_numero = int(input("Ingrese el número de socio que pagó todas las cuotas adeudadas: "))
        pagar_cuotas(socio_numero)
    elif opcion == "3":
        corregir_fecha_ingreso("13/03/2018", "14/03/2018")
    elif opcion == "4":
        nombre_apellido = input("Ingrese el nombre y apellido del socio a dar de baja: ")
        dar_de_baja(nombre_apellido)
    elif opcion == "5":
        imprimir_listado_socios()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
