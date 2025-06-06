import json
import os

path = os.path.dirname(os.path.abspath(__file__))

file = "/settings.json"

if not os.path.exists(path + file):
    file = "settings.json"
path += file
with open(path, "r") as f:
    settings = json.load(f)

print(settings.get("fontSize"))