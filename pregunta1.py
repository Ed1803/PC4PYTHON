import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Lanzará una excepción si hay un error en la solicitud
        data = response.json()  # Convertir la respuesta a formato JSON
        return data["bpi"]["USD"]["rate_float"]  # Obtener el precio actual de Bitcoin en USD
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin", e)
        return None

def main():
    # Solicitar al usuario la cantidad de bitcoins que posee
    cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que tiene: "))
    
    # Obtener el precio actual de Bitcoin en USD
    precio_bitcoin = obtener_precio_bitcoin()
    
    if precio_bitcoin is not None:
        # Calcular el costo en USD de la cantidad de bitcoins
        costo_en_usd = cantidad_bitcoins * precio_bitcoin
        
        # Mostrar el costo actual de "n" bitcoins en USD con cuatro decimales y separador de miles
        print(f"El costo actual de {cantidad_bitcoins} bitcoins en USD es: ${costo_en_usd:,.4f}")
    else:
        print("No se pudo obtener el precio actual de Bitcoin.")

if __name__ == "__main__":
    main()