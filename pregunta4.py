import requests

# Función para obtener el precio actual de Bitcoin desde la API de CoinDesk
def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate"]
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

# Obtener el precio actual de Bitcoin
precio_bitcoin = obtener_precio_bitcoin()

if precio_bitcoin:
    # Guardar el precio en un archivo de texto
    with open("precio_bitcoin.txt", "w") as archivo:
        archivo.write(f"Precio actual de Bitcoin en USD: {precio_bitcoin}\n")
    print("Datos del precio de Bitcoin registrado correctamente en 'precio_bitcoin.txt'.")
else:
    print("No se almacenaron datos.")
