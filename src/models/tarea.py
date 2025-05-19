from datetime import date
import storage.escritor_tareas as escritor_tareas

class Tarea:
    def __init__(self,id, titulo, id_usuario, descripcion='', fecha=None, repeticion=None, completada=False, fecha_completada=None):
        self.id = id                                                    # ID de la tarea, se incrementa automáticamente 
        self.titulo = titulo                                            # Título de la tarea
        self.id_usuario = id_usuario                                    # ID del usuario al que pertenece la tarea
        self.descripcion = descripcion                                  # Descripción opcional
        self.fecha = fecha or date.today()                              # Fecha programada (por defecto, hoy)
        self.repeticion = repeticion or "unica"                         # Puede ser 'diaria', 'semanal', 'mensual', 'unica'
        self.completada = completada or False                           # Estado de la tarea
        self.fecha_completada = fecha_completada or None                # Fecha de finalización

    def guardar_nueva(self):
        escritor_tareas.guardar_tarea(self)