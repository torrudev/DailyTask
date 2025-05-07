###
# Contiene las funciones para leer los datos de los archivos CSV
###

import os, csv

ARCHIVO_USUARIOS = "data/usuarios.csv"

# Esta función obtiene el último ID de usuario, devuelve None si el usuario ya existe
def obtener_ultimo_id_usuario(nombre_usuario):
    ultimo_id = 0

    # Verifica si el archivo de usuarios existe y no está vacío
    if (not os.path.isfile(ARCHIVO_USUARIOS) or os.path.getsize(ARCHIVO_USUARIOS) == 0):
        return ultimo_id
    
    # Lee el archivo CSV y buscar el último ID
    with open(ARCHIVO_USUARIOS, mode="r", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                # Si el nombre coincide devuelve None
                if fila["nombre"] == nombre_usuario:      
                    return None
                
                # Si el ID es mayor que el último ID, actualiza el último ID
                id_actual = int(fila["id"])
                if id_actual > ultimo_id:
                    ultimo_id = id_actual
            except (KeyError, ValueError):
                continue

    return ultimo_id

# Esta función devuelve el ID del usuario con el nombre introducido por parámetro, devuelve None si no existe o archivo vacio
def obtener_id_usuario(nombre_usuario):
    # Verifica si el archivo de usuarios existe y no está vacío
    if (not os.path.isfile(ARCHIVO_USUARIOS) or os.path.getsize(ARCHIVO_USUARIOS) == 0):
        return None
    
    with open(ARCHIVO_USUARIOS, mode="r", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["nombre"] == nombre_usuario:
                return int(fila["id"])
            
    return None

# Esta función devuelve una lista de diccionarios con los usuarios en el archivo CSV
def obtener_usuarios():
    usuarios = []

    # Verifica si el archivo de usuarios existe y no está vacío
    if (not os.path.isfile(ARCHIVO_USUARIOS) or os.path.getsize(ARCHIVO_USUARIOS) == 0):
        return None
    
    with open(ARCHIVO_USUARIOS, mode="r", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                id_usuario = int(fila["id"])
                nombre_usuario = fila["nombre"]
                usuarios.append({"id": id_usuario, "nombre": nombre_usuario})
            except (KeyError, ValueError):
                continue

    return usuarios