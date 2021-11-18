import json

f = open("weather.json")
weather = json.load(f)

with open("states-10m.json") as f:
    map = json.load(f)

map.update(weather)

with open("states-10m.json", "w") as f:
    json.dump(map, f)
