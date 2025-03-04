import json

# path = r"C:\sandbox\Python\fichier.txt"
# with open(path, "a", encoding="utf-8") as f:
#   f.write("\nVoila !")

# with open(path, "r", encoding="utf-8") as f:
#   content = f.read().splitlines()
#   print(content)
  
path = r"C:\sandbox\Python\fichier.json"

# with open(path, "r", encoding="utf-8") as f:
#   # json.dump({"name": "Python", "level": "hight"}, f)
#   content = json.load(f)
#   print(type((content)))
#   print(content)

with open(path, "r", encoding="utf-8") as f:
  data = json.load(f)
  print(data)
data.append(0)
data.append(1)
data.append(2)
data.append(3)
data.append(4)
data.append(5)
for i in data:
    data[i] = data[i] * 2
with open(path, "w", encoding="utf-8") as f:
  json.dump(data, f)
  print(data)