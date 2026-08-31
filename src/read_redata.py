import json

with open("data/raw/electricity.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for item in data["included"]:
    print(item["type"])

for item in data["included"]:
    for content_item in item["attributes"]["content"]:
        print(content_item["type"])
