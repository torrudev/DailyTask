###
# Esta clase representa un usuario en el sistema.
# Cada usuario tiene un ID único y un nombre, además de una lista de tareas.
###

import storage.csv_reader as lector_csv

class Usuario:
   
   # Constructor de la clase Usuario
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.tareas = []
    
    # Método de clase para crear un nuevo usuario comprobando si el nombre ya existe
    @classmethod
    def crear_nuevo(cls, nombre_usuario):
        id_usuario = lector_csv.obtener_ultimo_id_usuario(nombre_usuario)

        if id_usuario is None:
            raise ValueError(f"El nombre de usuario '{nombre_usuario}' ya existe.")
        
        return cls(id_usuario + 1, nombre_usuario)
    
    # Método de clase para cargar un usuario existente
    @classmethod
    def cargar(cls, nombre_usuario):
        id_usuario = lector_csv.obtener_id_usuario(nombre_usuario)

        if id_usuario is None:
            raise ValueError(f"El nombre de usuario '{nombre_usuario}' no existe.")

        return cls(id_usuario, nombre_usuario)