###
# main.py
# Esta es la entrada principal del programa.
###

import time

import prints.menus as menus
import validators.validador as validador
import utils.herramientas as herramientas

from models.usuario import Usuario
from models.tarea import Tarea

while True:
    # Llamar a la función de interfaz para mostrar el menú
    menus.mostrar_menu_inicial()
    
    # Pedir al usuario que seleccione una opción
    opcion = input("Selecciona una opción (0-3): ").strip()

    # Gestionar opción 1 (Nuevo usuario)
    if opcion == "1":
        try:
            nombre = input("Introduce tu nombre de usuario: ")
            id = validador.nombre_no_repetido(nombre) # devuelve último id + 1, lanza ValueError si el nombre ya existe

            nuevo_usuario = Usuario(id, nombre)
            nuevo_usuario.guardar_nuevo()

            print(f"👤 Usuario creado: {nuevo_usuario.nombre} (ID: {nuevo_usuario.id})")

        except ValueError as e:
            print(f"❌ Error: {e}")

    # Gestionar opción 2 (Iniciar sesión)
    elif opcion == "2":
        try:
            nombre = input("Introduce tu nombre de usuario: ")
            usuario_inicio_sesion = validador.usuario_existente(nombre) # devuelve objeto Usuario, lanza ValueError si no existe

            herramientas.limpiar_consola() # Limpiar la consola para una mejor visualización
            print(f"👤 Bienvenido de nuevo, {usuario_inicio_sesion.nombre} (ID: {usuario_inicio_sesion.id})")
        
            ###
            # LÓGICA TRAS INICIAR SESIÓN
            ###

            while True:
                menus.mostrar_menu_usuario()

                # Pedir al usuario que seleccione una opción
                opcion = input("Selecciona una opción (0-5): ").strip()

                # Gestionar opcion 1 (Crear tarea)
                if opcion == "1":
                    try:
                        # Obtener los parametros de la tarea introducidos por el usuario
                        nombre_tarea = input("Introduce el nombre de la tarea: ")
                        descripcion = input("Introduce una descripción (opcional): ")
                        repeticion = input("¿La tarea se repite? (diaria/semanal/mensual/unica): ").strip().lower()
                        if repeticion not in ["diaria", "semanal", "mensual", "unica"]:
                            raise ValueError("Repetición no válida. Debe ser 'diaria', 'semanal', 'mensual' o 'unica'.")
                        
                        # Generar id
                        id = validador.generar_id_tarea()

                        nueva_tarea = Tarea(id, nombre_tarea, usuario_inicio_sesion.id, descripcion, repeticion=repeticion)
                        nueva_tarea.guardar_nueva()

                        print(f"✅ Tarea creada: {nueva_tarea.titulo} (ID: {nueva_tarea.id})")

                    except ValueError as e:
                        print(f"❌ Error: {e}")

                # Gestionar opcion 2 (Ver tareas)
                elif opcion == "2":
                    try:
                        lista_tareas_usuario = validador.hay_tareas_usuario(usuario_inicio_sesion.id) # devuelve lista de tareas del usuario, lanza ValueError si no hay tareas para ese usuario
                        
                        print("\n📝 Lista de tareas:")
                        for tarea in lista_tareas_usuario:
                            print(f"\t·📄 {tarea.titulo}: {tarea.descripcion} (ID: {tarea.id}). Tarea {tarea.repeticion}({tarea.fecha}), Completada: {tarea.completada} - {tarea.fecha_completada}")

                    except ValueError as e:
                        print(f"❌ Error: {e}")

                # Gestionar opcion 3 (Ver tareas completadas)
                elif opcion == "3":
                    try:
                        lista_tareas_completadas = validador.hay_tareas_completadas_usuario(usuario_inicio_sesion.id) # devuelve lista de tareas completadas del usuario, lanza ValueError si no hay tareas completadas para ese usuario
                        
                        print("\n✅ Lista de tareas completadas:")
                        for tarea in lista_tareas_completadas:
                            print(f"\t·📄 {tarea.titulo}: {tarea.descripcion} (ID: {tarea.id}). Tarea {tarea.repeticion}({tarea.fecha}), Completada: {tarea.completada} - {tarea.fecha_completada}")
                    
                    except ValueError as e:
                        print(f"❌ Error: {e}")

                # Gestionar opcion 4 (Ver tareas pendientes)
                elif opcion == "4":
                    try:
                        lista_tareas_pendientes = validador.hay_tareas_pendientes_usuario(usuario_inicio_sesion.id) # devuelve lista de tareas pendientes del usuario, lanza ValueError si no hay tareas pendientes para ese usuario

                        print("\n📝 Lista de tareas pendientes:")
                        for tarea in lista_tareas_pendientes:
                            print(f"\t·📄 {tarea.titulo}: {tarea.descripcion} (ID: {tarea.id}). Tarea {tarea.repeticion}({tarea.fecha}), Completada: {tarea.completada} - {tarea.fecha_completada}")

                    except ValueError as e:
                        print(f"❌ Error: {e}")

                # Gestionar opcion 5 (Ver tareas para hoy)
                elif opcion == "5":
                    try:
                        pass
                    
                    except ValueError as e:
                        print(f"❌ Error: {e}")

                # Gestionar opción 0 (volver al menú principal)
                elif opcion == "0":
                    print("👋 Volviendo al menú principal...")
                    time.sleep(1.5)
                    herramientas.limpiar_consola()
                    break

                # Gestionar otras opciones
                else:
                    print("⚠️ Opción no válida. Recuerda introducir un número del 0 al 6.")

        except ValueError as e:
            print(f"❌ Error: {e}")

    # Gestionar opción 3 (Ver usuarios)
    elif opcion == "3":
        try:
            lista_usuarios = validador.hay_usuarios() # devuelve lista de usuarios, lanza ValueError si no hay usuarios

            print("\n👥 Lista de usuarios:")
            for usuario in lista_usuarios:
                print(f"\t·👤 Usuario: {usuario.nombre} (ID: {usuario.id})")
                
        except ValueError as e:
            print(f"❌ Error: {e}")              

    # Gestionar opción 0 (Salir)
    elif opcion == "0":
        print("👋 Saliendo del programa...")
        break

    # Gestionar otras opciones
    else:
        print("⚠️ Opción no válida. Recuerda introducir un número del 0 al 3.")