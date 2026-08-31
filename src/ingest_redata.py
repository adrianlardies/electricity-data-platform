# 1. CONFIGURACIÓN

import json
from pathlib import Path

import requests

# 2. REQUEST

output_dir = Path("data/raw/")
file_path = output_dir / "electricity.json"

print(output_dir.exists())
print(output_dir.is_file())
print(output_dir.is_dir())

url = "https://apidatos.ree.es/es/datos/balance/balance-electrico"

params = {
    "start_date": "2026-01-01T00:00",
    "end_date": "2026-01-31T23:59",
    "time_trunc": "day",
}

response = requests.get(url, params=params, timeout=10)

print(type(response))

status = response.status_code

print(status)

# 3. VALIDACIÓN,DECODING Y PERSISTENCIA/GUARDADO

try:
    response.raise_for_status()
    response_data = response.json()
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(response_data, file, indent=4, ensure_ascii=False)
except requests.exceptions.HTTPError:
    print("El servidor devolvió un error HTTP:", response.status_code)
except requests.exceptions.ConnectionError:
    print("No se pudo conectar con el servidor.")
except requests.exceptions.Timeout:
    print("El tiempo de respuesta es muy largo.")
