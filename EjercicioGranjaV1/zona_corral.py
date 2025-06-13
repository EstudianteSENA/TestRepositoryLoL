"""Esta es la clase Corral."""
class Corral:
    def __init__(self, identificador):
        self.identificador = identificador
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)
        print(f"{animal.nombre} fue agregado al corral {self.identificador}.")

    def hacer_limpieza(self):
        print(f"Corral {self.identificador} está limpio.")

    def mostrar_animales(self):
        print(f"Contenido del corral {self.identificador}:")
        for a in self.animales:
            print(f" - {a.nombre} ({a.tipo})")