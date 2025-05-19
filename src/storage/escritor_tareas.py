###
# Escritor del CSV tareas.
# Este módulo se encarga de escribir en el archivo CSV donde se almacenan las tareas.
###

###
# =========IMPORTS==========
###

import csv

import utils.herramientas as herramientas

# Ruta del archivo CSV
ARCHIVO_TAREAS = "data/tareas.csv"

###
# =========FUNCIONES==========
###

# Guarda una nueva tarea en el archivo CSV. Si el archivo está vacío, añade los encabezados.
def guardar_tarea(tarea):
    archivo_vacio = herramientas.no_existe_o_vacio(ARCHIVO_TAREAS)

    with open(ARCHIVO_TAREAS, mode="a", newline='', encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        if archivo_vacio:
            escritor.writerow(["id", "titulo", "descripcion", "fecha", "repeticion", "completada", "fecha_completada", "id_usuario"])
            
        escritor.writerow([tarea.id, tarea.titulo, tarea.descripcion, tarea.fecha, tarea.repeticion, tarea.completada, tarea.fecha_completada, tarea.id_usuario])