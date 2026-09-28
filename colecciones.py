# =================================================================
# ASIGNATURA: Fundamentos de Programación
# TEMA: Colecciones de datos (Uso de Diccionarios en Python)
# ESTUDIANTE: Ashley Mamallacta
# PARALELO: F
# =================================================================

def sistema_notas():
    # 1. Uso de colecciones: Inicialización del diccionario vacío
    # Relaciona nombres de estudiantes (claves) con sus notas (valores)
    registro_estudiantes = {}
    
    print("--- SISTEMA DE REGISTRO DE CALIFICACIONES ---")
    
    # 2. Funcionalidad: Agregar datos a la colección mediante un bucle
    while True:
        nombre = input("\nIngrese el nombre del estudiante (o escriba 'salir' para terminar): ").strip()
        if nombre.lower() == "salir":
            break
        
        try:
            nota = float(input(f"Ingrese la nota de {nombre} (0 - 10): "))
            if 0 <= nota <= 10:
                registro_estudiantes[nombre] = nota
                print(f"¡Estudiante {nombre} registrado con éxito!")
            else:
                print("Error: La nota debe estar en el rango de 0 a 10.")
        except ValueError:
            print("Error: Ingrese un número válido para la nota.")

    # 3. Funcionalidad: Mostrar la información almacenada en pantalla
    print("\n=================================================")
    print("       LISTA COMPLETA DE ESTUDIANTES Y NOTAS      ")
    print("=================================================")
    if not registro_estudiantes:
        print("No se registraron datos en el sistema.")
    else:
        # Recorremos el diccionario para mostrar los elementos
        for estudiante, calificacion in registro_estudiantes.items():
            print(f"Estudiante: {estudiante} | Nota Final: {calificacion}")
    print("=================================================")

    # 4. Operación básica adicional: Buscar elementos dentro del diccionario
    if registro_estudiantes:
        print("\n--- MÓDULO DE BÚSQUEDA DE CALIFICACIONES ---")
        buscar = input("Ingrese el nombre del estudiante que desea buscar: ").strip()
        if buscar in registro_estudiantes:
            print(f"¡Resultado encontrado! La nota de {buscar} es: {registro_estudiantes[buscar]}")
        else:
            print(f"El estudiante '{buscar}' no se encuentra en el registro.")

# Ejecución del programa principal
if __name__ == "__main__":
    sistema_notas()
