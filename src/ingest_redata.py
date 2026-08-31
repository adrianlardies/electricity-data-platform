# 1. CONFIGURACIÓN

import json

import requests

# 2. REQUEST

url = "https://apidatos.ree.es/es/datos/balance/balance-electrico?start_date=2026-01-01T00:00&end_date=2026-01-31T23:59&time_trunc=day"

response = requests.get(url)

print(type(response))

status = response.status_code

print(status)

# 3. VALIDACIÓN,DECODING Y PERSISTENCIA/GUARDADO

try:
    response.raise_for_status()
    response_data = response.json()
    with open("data/raw/electricity.json", "w", encoding="utf-8") as file:
        json.dump(response_data, file, indent=4, ensure_ascii=False)
except requests.exceptions.HTTPError as error:
    print(error)
