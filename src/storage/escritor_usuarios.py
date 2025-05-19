###
# Escritor del CSV usuarios.
# Este módulo se encarga de escribir en el archivo CSV donde se almacenan los usuarios.
###

###
# =========IMPORTS==========
###

import csv

import utils.herramientas as herramientas

# Ruta del archivo CSV
ARCHIVO_USUARIOS = "data/usuarios.csv"

###
# =========FUNCIONES==========
###

# Guarda un nuevo usuario en el archivo CSV. Si el archivo está vacío, añade los encabezados.
def guardar_usuario(usuario):
    archivo_vacio = herramientas.no_existe_o_vacio(ARCHIVO_USUARIOS)

    with open(ARCHIVO_USUARIOS, mode="a", newline='', encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        if archivo_vacio:
            escritor.writerow(["id", "nombre"])
            
        escritor.writerow([usuario.id, usuario.nombre])