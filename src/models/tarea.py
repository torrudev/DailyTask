from datetime import date

class Tarea:
    contador_id = 1 # ID de la tarea, se incrementa automáticamente

    def __init__(self, titulo, id_usuario, descripcion='', fecha=None, repeticion=None):
        self.id = Tarea.contador_id + 1               # ID de la tarea, se incrementa automáticamente 
        Tarea.contador_id += 1
        self.titulo = titulo                          # Título de la tarea
        self.id_usuario = id_usuario                  # ID del usuario al que pertenece la tarea
        self.descripcion = descripcion                # Descripción opcional
        self.fecha = fecha or date.today()            # Fecha programada (por defecto, hoy)
        self.repeticion = repeticion or "unica"       # Puede ser 'diaria', 'semanal', 'mensual', 'unica'
        self.completada = False                       # Estado de la tarea
        self.fecha_completada = None                  # Fecha de finalización