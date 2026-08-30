import requests

url = "https://apidatos.ree.es/es/datos/balance/balance-electrico?start_date=2026-01-01T00:00&end_date=2026-01-31T23:59&time_trunc=day"

response = requests.get(url)

print(type(response))

status = response.status_code

print(status)

text = response.text

print(type(text))

response_data = response.json()

print(type(response_data))
