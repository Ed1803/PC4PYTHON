def contar_lineas_codigo(archivo):
    try:
        # Verificar si la extensión del archivo es .py
        if not archivo.endswith('.py'):
            print("El archivo no tiene la extensión .py")
            return

        # Abrir el archivo en modo de lectura
        with open(archivo, 'r') as f:
            lineas = f.readlines()  # Leer todas las líneas del archivo

        # Contador para las líneas de código
        contar = 0

        # Recorrer cada línea del archivo
        for linea in lineas:
            linea = linea.strip()  # Eliminar espacios en blanco al inicio y al final
            # Verificar si la línea no está en blanco y no es un comentario
            if linea != '' and not linea.startswith('#'):
                contar += 1

        # Imprimir el resultado
        print(f"Archivo: {archivo}, número de líneas de código: {contar}")

    except FileNotFoundError:
        print("Archivo no encontrado.")

# Solicitar al usuario la ruta del archivo
ruta_archivo = input("Ingrese la ruta del archivo .py: ")

# Contar las líneas de código
contar_lineas_codigo(ruta_archivo)
