# Sistema de Gestión de Tareas Estudiantiles

tareas = []

def mostrar_menu():
    print("\n===== SISTEMA DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea():
    tarea = input("Escribe la tarea: ")
    tareas.append({"tarea": tarea, "estado": "Pendiente"})
    print("Tarea agregada correctamente.")

def ver_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    
    print("\nLista de tareas:")
    for i, t in enumerate(tareas):
        print(f"{i + 1}. {t['tarea']} - {t['estado']}")

def completar_tarea():
    ver_tareas()
    try:
        indice = int(input("Número de tarea completada: ")) - 1
        tareas[indice]["estado"] = "Completada"
        print("Tarea actualizada.")
    except:
        print("Opción inválida.")

def eliminar_tarea():
    ver_tareas()
    try:
        indice = int(input("Número de tarea a eliminar: ")) - 1
        tareas.pop(indice)
        print("Tarea eliminada.")
    except:
        print("Opción inválida.")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida")
