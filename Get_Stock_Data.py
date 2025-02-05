import yfinance as yf
from openpyxl import Workbook

def get_stock_data(ticker_symbol):
    # El símbolo de NVIDIA en Yahoo Finance es "NVDA"

    try:
        # Descargamos los datos del ticker
        stock = yf.Ticker(ticker_symbol)

        # Información general sobre el ticker
        info = stock.info
        print(f"Nombre: {info['shortName']}")
        print(f"Sector: {info['sector']}")
        print(f"Industria: {info['industry']}")
        print(f"Precio actual: ${info['currentPrice']}")
        print(f"Rango de 52 semanas: {info['fiftyTwoWeekLow']} - {info['fiftyTwoWeekHigh']}")

        # Opcional: Obtener datos históricos
        hist = stock.history(period="1y")  # Último mes de datos 1mo
        print("\nDatos históricos")
        print(hist)

        # Convert datetime index to naive datetimes (remove timezone)
        hist.index = hist.index.tz_localize(None)

        # Exportar los datos históricos a un archivo Excel
        filename = f"{ticker_symbol}_stock_data.xlsx"
        wb = Workbook()
        ws = wb.active

        # Escribir los encabezados
        headers = ["Date"] + list(hist.columns)
        ws.append(headers)

        # Escribir los datos
        for date, row in hist.iterrows():
            ws.append([date] + row.tolist())

        wb.save(filename)
        print(f"\nDatos exportados exitosamente a {filename}")

    except ImportError as e:
        print(f"Error de Importación: {e}")
    except ValueError as e:
        print(f"Error de Valor: {e}")
    except Exception as e:
        print(f"Error al obtener los datos: {e}")

# Llamamos a la función
get_stock_data("NVDA")
