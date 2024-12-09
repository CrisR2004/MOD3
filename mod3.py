from pymongo import MongoClient

# Configuración de la base de datos
client = MongoClient("mongodb://localhost:27017/")
db = client["recetario"]
recetas_collection = db["recetas"]

# Función para agregar una receta
def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes (separados por comas): ")
    pasos = input("Ingrese los pasos: ")
    nueva_receta = {
        "nombre": nombre,
        "ingredientes": ingredientes,
        "pasos": pasos
    }
    recetas_collection.insert_one(nueva_receta)
    print("Receta agregada exitosamente.\n")

# Función para actualizar una receta
def actualizar_receta():
    id_receta = input("Ingrese el ID de la receta a actualizar: ")
    receta = recetas_collection.find_one({"_id": id_receta})
    if receta:
        nombre = input("Ingrese el nuevo nombre de la receta: ")
        ingredientes = input("Ingrese los nuevos ingredientes (separados por comas): ")
        pasos = input("Ingrese los nuevos pasos: ")
        recetas_collection.update_one(
            {"_id": id_receta},
            {"$set": {"nombre": nombre, "ingredientes": ingredientes, "pasos": pasos}}
        )
        print("Receta actualizada exitosamente.\n")
    else:
        print("Receta no encontrada.\n")

# Función para eliminar una receta
def eliminar_receta():
    id_receta = input("Ingrese el ID de la receta a eliminar: ")
    receta = recetas_collection.find_one({"_id": id_receta})
    if receta:
        recetas_collection.delete_one({"_id": id_receta})
        print("Receta eliminada exitosamente.\n")
    else:
        print("Receta no encontrada.\n")

# Función para ver todas las recetas
def ver_recetas():
    recetas = recetas_collection.find()
    print("\nListado de recetas:")
    for receta in recetas:
        print(f"{receta['_id']} - {receta['nombre']}")
    print()

# Función para buscar los ingredientes y pasos de una receta
def buscar_receta():
    id_receta = input("Ingrese el ID de la receta que desea buscar: ")
    receta = recetas_collection.find_one({"_id": id_receta})
    if receta:
        print(f"\nReceta: {receta['nombre']}\nIngredientes: {receta['ingredientes']}\nPasos: {receta['pasos']}\n")
    else:
        print("Receta no encontrada.\n")

# Función para mostrar el menú
def mostrar_menu():
    print("Seleccione una opción:")
    print("a) Agregar nueva receta")
    print("b) Actualizar receta existente")
    print("c) Eliminar receta existente")
    print("d) Ver listado de recetas")
    print("e) Buscar ingredientes y pasos de receta")
    print("f) Salir")

# Función principal para ejecutar el programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ").lower()

        if opcion == 'a':
            agregar_receta()
        elif opcion == 'b':
            actualizar_receta()
        elif opcion == 'c':
            eliminar_receta()
        elif opcion == 'd':
            ver_recetas()
        elif opcion == 'e':
            buscar_receta()
        elif opcion == 'f':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

    # Cerrar la conexión a la base de datos al salir
    client.close()

# Ejecutar el programa
main()
