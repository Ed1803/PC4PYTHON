import requests
from zipfile import ZipFile
from io import BytesIO

# Función para descargar la imagen desde la URL
def descargar_imagen(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

# Función para guardar la imagen en un archivo zip
def guardar_en_zip(nombre_archivo, contenido):
    with ZipFile(nombre_archivo, 'w') as archivo_zip:
        archivo_zip.writestr("imagen_descargada.jpg", contenido)

# Función para extraer la imagen de un archivo zip
def extraer_de_zip(nombre_archivo_zip):
    with ZipFile(nombre_archivo_zip, 'r') as archivo_zip:
        archivo_zip.extractall()

# URL de la imagen a descargar
url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Descargar la imagen
contenido_imagen = descargar_imagen(url_imagen)
if contenido_imagen:
    print("Imagen descargada exitosamente.")

    # Guardar la imagen en un archivo zip
    nombre_archivo_zip = "imagen.zip"
    guardar_en_zip(nombre_archivo_zip, contenido_imagen)
    print(f"Imagen guardada como '{nombre_archivo_zip}'.")

    # Extraer la imagen del archivo zip
    extraer_de_zip(nombre_archivo_zip)
    print("Imagen extraída correctamente.")

else:
    print("No se pudo descargar la imagen.")