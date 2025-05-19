###
# Lector del CSV usuarios.
# Este módulo se encarga de leer el archivo CSV donde se almacenan los usuarios.
###

###
# =========IMPORTS==========
###

import csv

import utils.herramientas as herramientas

from models.tarea import Tarea

# Ruta del archivo CSV
ARCHIVO_TAREAS = "data/tareas.csv"

###
# =========FUNCIONES==========
###

# Devuelve el último ID usado en el archivo CSV. Si el archivo está vacío, devuelve 0.
def ultimo_id():
    ultimo_id = 0

    if herramientas.no_existe_o_vacio(ARCHIVO_TAREAS):
        return ultimo_id
    
    with open(ARCHIVO_TAREAS, mode="r", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                id_tarea = int(fila["id"])
                if id_tarea > ultimo_id:
                    ultimo_id = id_tarea
            except (KeyError, ValueError):
                continue

    return ultimo_id

# Devuelve una lista de objetos Tarea con todos las tareas del usuario, devuelve None si el archivo está vacío.
def obtener_todas_tareas_usuario(id_usuario):
    lista_tareas = []

    if herramientas.no_existe_o_vacio(ARCHIVO_TAREAS):
        return None
    
    with open(ARCHIVO_TAREAS, mode="r", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                if fila["id_usuario"] == id_usuario:
                    lista_tareas.append(Tarea(fila["id"], fila["titulo"], fila["id_usuario"], fila["descripcion"], fila["fecha"], fila["repeticion"], fila["completada"], fila["fecha_completada"]))
            except (KeyError, ValueError):
                continue

    return lista_tareas

# Devuelve una lista de objetos Tarea con todos las tareas completadas del usuario, devuelve None si el archivo está vacío.
def obtener_todas_tareas_completadas_usuario(id_usuario):
    lista_tareas_completadas = []

    if herramientas.no_existe_o_vacio(ARCHIVO_TAREAS):
        return None
    
    with open(ARCHIVO_TAREAS, mode="r", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                if fila["id_usuario"] == id_usuario and fila["completada"] == "True":
                    lista_tareas_completadas.append(Tarea(fila["id"], fila["titulo"], fila["id_usuario"], fila["descripcion"], fila["fecha"], fila["repeticion"], fila["completada"], fila["fecha_completada"]))
            except (KeyError, ValueError):
                continue

    return lista_tareas_completadas

# Devuelve una lista de objetos Tarea con todos las tareas pendientes del usuario, devuelve None si el archivo está vacío.
def obtener_todas_tareas_pendientes_usuario(id_usuario):
    lista_tareas_pendientes = []

    if herramientas.no_existe_o_vacio(ARCHIVO_TAREAS):
        return None
    
    with open(ARCHIVO_TAREAS, mode="r", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                if fila["id_usuario"] == id_usuario and fila["completada"] == "False":
                    lista_tareas_pendientes.append(Tarea(fila["id"], fila["titulo"], fila["id_usuario"], fila["descripcion"], fila["fecha"], fila["repeticion"], fila["completada"], fila["fecha_completada"]))
            except (KeyError, ValueError):
                continue

    return lista_tareas_pendientes