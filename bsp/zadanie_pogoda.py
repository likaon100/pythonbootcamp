import json
from urllib.request import urlopen

gdzie = input("Podaj lokalizacje:")

with urlopen(f"https://www.metaweather.com/api/location/search/?query={gdzie}") as file:
    data = json.loads(file.read().decode("utf-8"))
print(data)
print(data[0]["woeid"])

with urlopen(f"https://www.metaweather.com/api/location/{woeid}") as file:
    data = json.loads(file.read().decode("utf-8"))
print(data)




