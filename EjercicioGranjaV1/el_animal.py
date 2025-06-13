"""Esta es la clase animal."""
class Animal:
    def __init__(self, tipo, peso=0):
        self.tipo = tipo
        self.peso = peso
        self.nombre = "Sin nombre"
        self.vacunado = False

    def alimentar(self, cantidad):
        self.peso += cantidad * 0.12  
        print(f"Se alimentó a {self.nombre} con {cantidad}kg. Peso actual: {self.peso:.2f}kg")

    def vacunar(self):
        self.vacunado = True
        print(f"{self.nombre} ha recibido su vacuna.")

    def registrar_peso(self):
        print(f"Registro: {self.nombre} pesa {self.peso:.2f}kg")