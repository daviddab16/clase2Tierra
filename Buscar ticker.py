import requests
from bs4 import BeautifulSoup


def buscar_tickers(nombre_empresa):
    """
    Busca los tickers de las empresas que coinciden con el nombre proporcionado.

    Args:
        nombre_empresa (str): El nombre de la empresa a buscar.

    Returns:
        list: Una lista de tuplas que contienen el símbolo y el nombre de cada empresa.
    """

    # URL de búsqueda de Yahoo Finance
    url = f"https://finance.yahoo.com/search?q={nombre_empresa}"

    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
    except requests.exceptions.RequestException as err:
        print(f"Error al realizar la solicitud HTTP: {err}")
        return []

    # Parsear el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar la tabla de resultados
    tabla = soup.find('table', {'class': 'simpTbl'})

    if not tabla:
        print("No se encontraron resultados")
        return []

    # Extraer los tickers y nombres de las empresas
    tickers = []
    for fila in tabla.find_all('tr')[1:]:  # Saltar la primera fila (cabecera)
        celdas = fila.find_all('td')
        if len(celdas) >= 2:
            simbolo = celdas[0].text.strip()
            nombre = celdas[1].text.strip()
            tickers.append((simbolo, nombre))

    return tickers


# Ejemplo de uso
nombre_empresa = "Apple"
tickers = buscar_tickers(nombre_empresa)

if tickers:
    print(f"Resultados de búsqueda para '{nombre_empresa}':")
    for simbolo, nombre in tickers:
        print(f"Símbolo: {simbolo}, Nombre: {nombre}")
else:
    print("No se encontraron tickers para la búsqueda.")