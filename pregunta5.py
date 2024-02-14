def guardar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as archivo:
            for i in range(1, 11):
                archivo.write(f"{numero} x {i} = {numero * i}\n")
        print(f"Tabla de multiplicar del {numero} guardada correctamente en tabla-{numero}.txt")
    except Exception as e:
        print(f"Error al guardar la tabla de multiplicar: {e}")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            print(f"Tabla de multiplicar del {numero}:")
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= linea <= len(lineas):
                print(f"Línea {linea} de la tabla de multiplicar del {numero}:")
                print(lineas[linea - 1].strip())
            else:
                print(f"No existe la línea {linea} en la tabla de multiplicar del {numero}.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def main():
    while True:
        print("\nMenu:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "2":
            numero = int(input("Ingrese el numero de la tabla de multiplicar: "))
            if 1 <= numero <= 10:
                mostrar_tabla_multiplicar(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "3":
            numero = int(input("Ingrese el numero de la tabla de multiplicar: "))
            linea = int(input("Ingrese el número de línea a mostrar: "))
            if 1 <= numero <= 10 and 1 <= linea <= 10:
                mostrar_linea_tabla_multiplicar(numero, linea)
            else:
                print("El número y la línea deben estar entre 1 y 10.")
        elif opcion == "4":
            print("ADIOS")
            break
        else:
            print("Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
