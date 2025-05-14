###
# Esta clase representa una tarea en el sistema.
# Cada tarea tiene un ID único, un título, una descripción opcional, una fecha programada, un estado de completada y un ID de usuario asociado.
###
from datetime import date
import storage.csv_reader as lector_csv

class Tarea:

    def __init__(self, titulo, id_usuario, descripcion='', fecha=None, repeticion=None):
        self.id = lector_csv.obtener_ultimo_id_tarea() + 1      # ID de la tarea, se incrementa automáticamente 
        self.titulo = titulo                                    # Título de la tarea
        self.id_usuario = id_usuario                            # ID del usuario al que pertenece la tarea
        self.descripcion = descripcion                          # Descripción opcional
        self.fecha = fecha or date.today()                      # Fecha programada (por defecto, hoy)
        self.repeticion = repeticion or "unica"                 # Puede ser 'diaria', 'semanal', 'mensual', 'unica'
        self.completada = False                                 # Estado de la tarea
        self.fecha_completada = None                            # Fecha de finalización