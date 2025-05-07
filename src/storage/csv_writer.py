###
# Contiene las funciones para escribir los datos de los archivos CSV
###

import os, csv

ARCHIVO_USUARIOS = "data/usuarios.csv"

# Guardar el usuario en el archivo CSV
def guardar_usuario(usuario):
    # Devuelve True si el archivo no existe o está vacío, de lo contrario devuelve False
    escribir_cabecera = (not os.path.isfile(ARCHIVO_USUARIOS) or os.path.getsize(ARCHIVO_USUARIOS) == 0)

    # IMPORTANTE: Hay que comprobar si el archivo existe antes de ejecutar 'open' ya que si no existe, se crea uno nuevo.
    # El modo "a" (append) no sobrescribe el archivo, sino que añade al final.
    with open(ARCHIVO_USUARIOS, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)

        if escribir_cabecera:
            writer.writerow(["id", "nombre"])
            
        writer.writerow([usuario.id, usuario.nombre])