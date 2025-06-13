# Importación de clases
from el_animal import Animal
from la_granja import SistemaGranja
from trabajador import Trabajador
from zona_corral import Corral

# Crear la granja
granja = SistemaGranja("El Buen Pastor")

# Crear empleados
empleado1 = Trabajador("Lucía", "EMP001")
empleado2 = Trabajador("Carlos", "EMP002")

# Registrar empleados en la granja
granja.registrar_empleado(empleado1)
granja.registrar_empleado(empleado2)

# Marcar asistencia y realizar tareas
empleado1.marcar_asistencia()
empleado1.agregar_tarea("Alimentar a los animales")
empleado2.marcar_asistencia()
empleado2.agregar_tarea("Limpieza de corrales")

# Crear corrales
corral_vacas = Corral("V-01")
corral_cerdos = Corral("C-01")

# Incluir corrales en la granja
granja.incluir_corral(corral_vacas)
granja.incluir_corral(corral_cerdos)

# Crear animales
vaca1 = Animal("Vaca", peso=300)
vaca1.nombre = "Lola"
cerdo1 = Animal("Cerdo", peso=100)
cerdo1.nombre = "Chanchito"

# Alimentar y vacunar animales
vaca1.alimentar(20)
vaca1.vacunar()
vaca1.registrar_peso()

cerdo1.alimentar(10)
cerdo1.vacunar()
cerdo1.registrar_peso()

# Asignar animales a corrales
corral_vacas.agregar_animal(vaca1)
corral_cerdos.agregar_animal(cerdo1)

# Mostrar animales por corral
corral_vacas.mostrar_animales()
corral_cerdos.mostrar_animales()

# Limpieza de corrales
corral_vacas.hacer_limpieza()
corral_cerdos.hacer_limpieza()

# Reportar una incidencia
empleado2.anotar_incidencia("Puerta del corral C-01 quedó abierta.")

# Finalizar operación de la granja
granja.finalizar_operacion()
