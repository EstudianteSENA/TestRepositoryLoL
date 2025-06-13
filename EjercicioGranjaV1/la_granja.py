"""Esta es la clase granja."""
class SistemaGranja:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_corrales = []
        self.personal = []

    def incluir_corral(self, corral):
        self.lista_corrales.append(corral)
        print(f"Se añadió el corral {corral.identificador} a {self.nombre}.")

    def registrar_empleado(self, trabajador):
        self.personal.append(trabajador)
        print(f"{trabajador.nombre} ahora trabaja en {self.nombre}.")

    def finalizar_operacion(self):
        print(f"{self.nombre} ha cesado actividades. Personal liberado.")
        self.personal.clear()