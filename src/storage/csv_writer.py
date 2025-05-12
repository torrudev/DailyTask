###
# Contiene las funciones para escribir los datos de los archivos CSV
###

import os, csv

ARCHIVO_USUARIOS = "data/usuarios.csv"
ARCHIVO_TAREAS = "data/tareas.csv"

# Guardar el usuario en el archivo CSV
def guardar_usuario(usuario):
    # Devuelve True si el archivo no existe o está vacío, de lo contrario devuelve False
    escribir_cabecera = (not os.path.isfile(ARCHIVO_USUARIOS) or os.path.getsize(ARCHIVO_USUARIOS) == 0)

    # IMPORTANTE: Hay que comprobar si el archivo existe antes de ejecutar 'open' ya que si no existe, se crea uno nuevo.
    # El modo "a" (append) no sobrescribe el archivo, sino que añade al final.
    with open(ARCHIVO_USUARIOS, mode="a", newline='', encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        if escribir_cabecera:
            escritor.writerow(["id", "nombre"])
            
        escritor.writerow([usuario.id, usuario.nombre])

# Guardar la tarea en el archivo CSV
def guardar_tarea(tarea):
    # Devuelve True si el archivo no existe o está vacío, de lo contrario devuelve False
    escribir_cabecera = (not os.path.isfile(ARCHIVO_TAREAS) or os.path.getsize(ARCHIVO_TAREAS) == 0)

    # IMPORTANTE: Hay que comprobar si el archivo existe antes de ejecutar 'open' ya que si no existe, se crea uno nuevo.
    # El modo "a" (append) no sobrescribe el archivo, sino que añade al final.
    with open(ARCHIVO_TAREAS, mode="a", newline='', encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        if escribir_cabecera:
            escritor.writerow(["id", "titulo", "descripcion", "fecha", "repeticion", "completada", "fecha_completada", "id_usuario"])
            
        escritor.writerow([tarea.id, tarea.titulo, tarea.descripcion, tarea.fecha, tarea.repeticion, tarea.completada, tarea.fecha_completada, tarea.id_usuario])