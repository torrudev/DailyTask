###
# Main.py
###

from models.usuario import Usuario
import storage.csv_reader as lector_csv
import storage.csv_writer as escritor_csv

# Función para imprimir el menú principal
def mostrar_menu_usuario():
    print("\n-------- Menú Login --------")
    print("1. Nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Ver usuarios")
    print("4. Salir")
    print("----------------------------")

while True:
    # Llamar a la función para mostrar el menú de usuario
    mostrar_menu_usuario()
    opcion = input("Selecciona una opción (1-4): ").strip()

    # Opción para crear un nuevo usuario
    if opcion == "1":
        try:
            # Crear una instancia de Usuario
            nombre_usuario = input("Introduce tu nombre de usuario: ")
            usuario_nuevo = Usuario.crear_nuevo(nombre_usuario)

            # Guardar el nuevo usuario en el archivo CSV  
            escritor_csv.guardar_usuario(usuario_nuevo)
            print(f"👤 Usuario creado: {usuario_nuevo.nombre} (ID: {usuario_nuevo.id})")
        
        except ValueError as e:
            print(f"❌ Error: {e}")

    #Opción para iniciar sesión
    elif opcion == "2":
        try:
            # Crear una instancia de Usuario
            nombre_usuario = input("Introduce tu nombre de ususario: ")
            usuario_cargado = Usuario.cargar(nombre_usuario)

            # Imprimir el mensaje de bienvenida
            print(f"👤 Bienvenido de nuevo, {usuario_cargado.nombre} (ID: {usuario_cargado.id})")

        except ValueError as e:
            print(f"❌ Error: {e}")

    # Opción para ver un listado de todos los usuarios, en caso de que no haya ninguno, se muestra un mensaje
    elif opcion == "3":
        usuarios = lector_csv.obtener_usuarios()

        # Verifica si hay usuarios registrados
        if usuarios is None:
            print("❌ No hay usuarios registrados.")
            continue
        
        # Imprimir la lista de usuarios
        print("\n👥 Lista de usuarios registrados:")
        for usuario in usuarios:
            print(f"\t·👤 Usuario: {usuario['nombre']} (ID: {usuario['id']})")

    # Opción salir del programa
    elif opcion == "4":
        print("👋 Saliendo del programa...")
        break

    else:
        print("⚠️ Opción no válida. Recuerda introducir un número del 1 al 5.")