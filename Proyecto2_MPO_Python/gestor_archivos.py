import os
from datetime import datetime

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Crear un archivo de texto")
    print("4. Escribir texto en un archivo existente")
    print("5. Eliminar un archivo o directorio")
    print("6. Mostrar información del archivo")
    print("7. Salir")

def listar_contenido():
    try:
        elementos = os.listdir()
        if not elementos:
            print("El directorio está vacío.")
        else:
            print("\nContenido del directorio:")
            for elemento in elementos:
                ruta = os.path.join(os.getcwd(), elemento)
                if os.path.isdir(ruta):
                    print(f"[Carpeta] {elemento}")
                elif os.path.isfile(ruta):
                    print(f"[Archivo] {elemento}")
                else:
                    print(f"[Desconocido] {elemento}")
    except Exception as e:
        print(f"Error al listar el contenido: {e}")                        

def crear_directorio():
    nombre = input("Introduce el nombre del nuevo directorio: ").strip()
    if not nombre:
        print("No se ha introducido ningún nombre.")
        return
    if os.path.exists(nombre):
        print("Ya existe un archivo o carpeta con ese nombre.")
    else:
        try:
            os.mkdir(nombre)
            print(f"Directorio '{nombre}' creado correctamente.")
        except Exception as e:
            print(f"No se pudo crear el directorio: {e}")

def crear_archivo():
    nombre = input("Introduce el nombre del archivo (.txt): ").strip()
    if os.path.exists(nombre):
        print("Ya existe un archivo con ese nombre. ")
    else:
        contenido = input("Escribe el contenido del archivo:\n")
        try:
            with open(nombre, "w", encoding="utf-8") as archivo:
                archivo.write(contenido)
            print(f"Archivo '{nombre}' creado.")
        except Exception as e:
            print(f"No se pudo crear el archivo: {e}")


def escribir_en_archivo():
    nombre= input("Introduce el nombre del archivo existente (.txt): ").strip()
    if not os.path.isfile(nombre):
        print("Archivo no encontrado. ")
        return
    texto = input("Escribe el texto que quieres añadir al archivo:\n")
    try:
        with open(nombre, "a", encoding="utf-8") as archivo:
            archivo.write("\n" + texto)
        print(f"Texto añadido al archivo '{nombre}'.")
    except Exception as e:
        print(f"No se pudo escribir en el archivo: {e}")    

def eliminar_elemento():
    nombre = input("Introduce el nombre del archivo a eliminar: ").strip()
    if not os.path.exists(nombre):
        print("Archivo no encontrado. ")
        return
    try:
        if os.path.isfile(nombre):
            os.remove(nombre)
            print(f"Archivo '{nombre}' eliminado.")
        elif os.path.isdir(nombre):
            os.rmdir(nombre)
            print(f"Directorio '{nombre}' eliminado.")
        else:
            print("El archivo o directorio no es válido. ")
    except Exception as e:
        print(f"No se pudo eliminar el archivo o directorio: {e}")

def mostrar_informacion():
    nombre = input("Introduce el nombre del archivo o directorio: ").strip()
    if not os.path.exists(nombre):
        print("Archivo o directorio no encontrado. ")
        return 
    try:
        tipo = "Archivo" if os.path.isfile(nombre) else "Carpeta" if os.path.isdir(nombre) else "Desconocido"
        tamaño = os.path.getsize(nombre)
        fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(nombre)).strftime("%Y-%m-%d %H:%M:%S")

        print(f"\nInformación de '{nombre}':")
        print(f"Tipo: {tipo}")
        print(f"Tamaño: {tamaño} bytes")
        print(f"Fecha de última modificación: {fecha_modificacion}")

    except Exception as e:
        print(f"No se pudo obtener la información: {e}")


def main():
    while True:
        print(f"\nRuta actual: {os.getcwd()}")
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            listar_contenido()
        elif opcion == "2":
            crear_directorio()
        elif opcion == "3":
            crear_archivo()
        elif opcion == "4":
            escribir_en_archivo()
        elif opcion == "5":
            eliminar_elemento()
        elif opcion == "6":
            mostrar_informacion()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()