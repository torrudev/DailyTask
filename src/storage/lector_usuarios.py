###
# Lector del CSV usuarios.
# Este módulo se encarga de leer el archivo CSV donde se almacenan los usuarios.
###

###
# =========IMPORTS==========
###

import csv

import utils.herramientas as herramientas

from models.usuario import Usuario

# Ruta del archivo CSV
ARCHIVO_USUARIOS = "data/usuarios.csv"

###
# =========FUNCIONES==========
###

# Encuentra un usuario por el nombre, devuelve un objeto Usuario si lo encuentra, de lo contrario devuelve None.
def encontrar_usuario(nombre):

    if herramientas.no_existe_o_vacio(ARCHIVO_USUARIOS):
        return None
    
    with open(ARCHIVO_USUARIOS, mode="r", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                if fila["nombre"] == nombre:
                    return Usuario(fila["id"], fila["nombre"])
            except (KeyError, ValueError):
                continue    

    return None

# Devuelve el último ID usado en el archivo CSV. Si el archivo está vacío, devuelve 0.
def ultimo_id():
    ultimo_id = 0

    if herramientas.no_existe_o_vacio(ARCHIVO_USUARIOS):
        return ultimo_id
    
    with open(ARCHIVO_USUARIOS, mode="r", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                id_usuario = int(fila["id"])
                if id_usuario > ultimo_id:
                    ultimo_id = id_usuario
            except (KeyError, ValueError):
                continue

    return ultimo_id

# Devuelve una lista de objetos Usuario con todos los usuarios del archivo CSV, devuelve None si el archivo está vacío.
def obtener_todos_usuarios():
    lista_usuarios = []

    if herramientas.no_existe_o_vacio(ARCHIVO_USUARIOS):
        return None
    
    with open(ARCHIVO_USUARIOS, mode="r", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                lista_usuarios.append(Usuario(fila["id"], fila["nombre"]))
            except (KeyError, ValueError):
                continue

    return lista_usuarios