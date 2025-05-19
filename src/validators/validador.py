import storage.lector_usuarios as lector_usuarios
import storage.lector_tareas as lector_tareas

# Devuelve el ultimo id de usuario si el nombre no está repetido, de lo contrario lanza un ValueError
def nombre_no_repetido(nombre):
    if lector_usuarios.encontrar_usuario(nombre) is None:
        return lector_usuarios.ultimo_id() + 1
    else:
        raise ValueError("⚠️ El nombre de usuario ya existe. Por favor, elige otro.")
    
# Devuelve una lista de usuarios si hay usuarios guardados, de lo contrario lanza un ValueError
def hay_usuarios():
    lista_usuarios = lector_usuarios.obtener_todos_usuarios()

    if lista_usuarios is None or len(lista_usuarios) == 0:
        raise ValueError("⚠️ Todavía no hay usuarios guardados.")
    else:
        return lista_usuarios
    
# Devuelve un Usuario si el nombre existe, de lo contrario lanza un ValueError
def usuario_existente(nombre):
    usuario = lector_usuarios.encontrar_usuario(nombre)

    if usuario is not None:
        return usuario
    else: 
        raise ValueError("⚠️ El usuario no existe. Por favor, verifica el nombre introducido.")
    
# Generar el id 
def generar_id_tarea():
    return lector_tareas.ultimo_id() + 1

# Devuelve una lista de tareas si hay tareas asignadas al usuario, de lo contrario lanza un ValueError
def hay_tareas_usuario(id_usuario):
    lista_tareas = lector_tareas.obtener_todas_tareas_usuario(id_usuario)

    if lista_tareas is None or len(lista_tareas) == 0:
        raise ValueError("⚠️ Todavía no hay tareas para este usuario.")
    else:
        return lista_tareas
    
# Devuelve una lista de tareas completadas por el usuario, de lo contrario lanza un ValueError
def hay_tareas_completadas_usuario(id_usuario):
    lista_tareas_completadas = lector_tareas.obtener_todas_tareas_completadas_usuario(id_usuario)

    if lista_tareas_completadas is None or len(lista_tareas_completadas) == 0:
        raise ValueError("⚠️ Todavía no hay tareas completadas para este usuario.")
    else:
        return lista_tareas_completadas

# Devuelve una lista de tareas completadas por el usuario, de lo contrario lanza un ValueError
def hay_tareas_pendientes_usuario(id_usuario):
    lista_tareas_pendientes = lector_tareas.obtener_todas_tareas_pendientes_usuario(id_usuario)

    if lista_tareas_pendientes is None or len(lista_tareas_pendientes) == 0:
        raise ValueError("⚠️ Todavía no hay tareas pendientes para este usuario.")
    else:
        return lista_tareas_pendientes