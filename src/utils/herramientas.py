import os

# True si el archivo no existe o está vacío
def no_existe_o_vacio(archivo):
    return (not os.path.isfile(archivo) or os.path.getsize(archivo) == 0)

# Función para limpiar la terminal
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')