from pyfiglet import Figlet
import random

# Función para obtener una fuente aleatoria si no se especifica ninguna
def obtener_fuente_aleatoria():
    figlet = Figlet()
    fuentes = figlet.getFonts()
    return random.choice(fuentes)

try:
    # Solicitar al usuario el nombre de la fuente
    nombre_fuente = input("Ingrese el nombre de la fuente (dejar en blanco para una selección aleatoria): ").strip()
    if not nombre_fuente:
        nombre_fuente = obtener_fuente_aleatoria()

    # Solicitar al usuario el texto a imprimir
    texto = input("Ingrese el texto: ")

    # Crear una instancia de Figlet y establecer la fuente seleccionada
    figlet = Figlet(font=nombre_fuente)

    # Imprimir el texto utilizando la fuente seleccionada
    print(figlet.renderText(texto))

except KeyboardInterrupt:
    print("\nSe ha interrumpido la ejecución del programa.")
except Exception as e:
    print(f"Se ha producido un error: {e}")
