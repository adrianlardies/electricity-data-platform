# 1. Configuración/Input

import json
from pathlib import Path

import requests

output_dir = Path("data/raw/")

file_path = output_dir / "electricity.json"

url = "https://apidatos.ree.es/es/datos/balance/balance-electrico"

params = {
    "start_date": "2026-01-01T00:00",
    "end_date": "2026-01-31T23:59",
    "time_trunc": "day",
}

# 2. Obtener los datos desde REData


def obtain_json():
    try:
        response = requests.get(url, params=params, timeout=10)
        status = response.status_code
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("El servidor devolvió un error HTTP:", status)
    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con el servidor.")
    except requests.exceptions.Timeout:
        print("El tiempo de respuesta es muy largo.")
    return response


# 3. Guardar los datos obtenidos como raw JSON


def save_json(response):
    response_data = response.json()
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(response_data, file, indent=4, ensure_ascii=False)


obtain_json()
save_json(obtain_json())
