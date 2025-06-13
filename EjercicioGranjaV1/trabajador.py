"""Esta es la clase trabajador."""
class Trabajador:
    def __init__(self, nombre, codigo_empleado):
        self.nombre = nombre
        self.codigo_empleado = codigo_empleado
        self.actividades = []
        self.asistencias = 0
        self.problemas = []

    def agregar_tarea(self, tarea):
        self.actividades.append(tarea)
        print(f"{self.nombre} completó la actividad: {tarea}.")

    def marcar_asistencia(self):
        self.asistencias += 1
        print(f"Asistencia anotada para {self.nombre}. Total: {self.asistencias}")

    def anotar_incidencia(self, detalle):
        self.problemas.append(detalle)
        print(f"{self.nombre} informó: {detalle}")