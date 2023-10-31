class Motocicleta:
    new = True  # Atributo de clase para especificar que todas las motocicletas son nuevas
    engine = False
    def __init__(self, color, license_plate, fuel, number_wheel, brand, model, date_manufacture, top_speed, weight):
        self.color = color
        self.license_plate = license_plate
        self.fuel = fuel
        self.number_wheel = number_wheel
        self.brand = brand
        self.model = model
        self.date_manufacture = date_manufacture
        self.top_speed = top_speed
        self.weight = weight

    def start_engine(self):
        if self.engine == False:
            print("el motor ha arrancado")
            self.engine = True
        else:
            print("el motor ya estaba en marcha")

    def stop_engine(self):
        if self.engine == True:
            print("El motor se ha detenido")
            self.engine = False
        else:
            print("El motor ya estaba detenido")

    def ask_price(self):
        print(f"El precio de esta motocicleta es $ {price_moto}")

# Ejemplo de cómo crear una instancia de Motocicleta
mi_motocicleta = Motocicleta("Rojo", "1234XYZ", 10, 2, "Honda", "CBR1000RR", "2023-01-15", 280, 200)
mi_motocicleta2 = Motocicleta ("Negro", "1234XYZ", 10, 2, "Honda", "CBR1000RR", "2023-01-15", 280, 200)

mi_motocicleta.start_engine()
mi_motocicleta2.start_engine()
mi_motocicleta2.stop_engine()
mi_motocicleta.stop_engine()

mi_motocicleta.price = 800000
print(f"El precio de la motocicleta '{mi_motocicleta.brand} {mi_motocicleta.model}' es de ${mi_motocicleta.price}"  )
price_moto = mi_motocicleta.ask_price()
print(f"El precio de la motocicleta es ${price_moto}")
price_moto2 = mi_motocicleta2.ask_price()
