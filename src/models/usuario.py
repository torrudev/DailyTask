import storage.escritor_usuarios as escritor_usuarios

class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def guardar_nuevo(self):
        escritor_usuarios.guardar_usuario(self)