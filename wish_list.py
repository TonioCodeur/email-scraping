import json

wish_list = []

with open('wish_list.json') as f:
    wish_list = json.load(f)

run = True
while run:
  print("bienvenue dans vôtrre wish list")
  print("tapez 1 si vous voulez ajouter un item")
  print("tapez 2 si vous voulez supprimer un item")
  print("tapez 3 si vous voulez afficher tous les items")
  print("tapez 4 si vous voulez quitter")
  choix = input()
  if choix.isdigit():
    if int(choix) == 1:
      print("tapez le nom de l'item que vous voulez ajouter")
      nom = input()
      wish_list.append(nom)
      with open('wish_list.json', 'w') as f:
        json.dump(wish_list, f, ensure_ascii=False)
    elif int(choix) == 2:
      print("tapez le nom de l'item que vous voulez supprimer")
      nom = input()
      wish_list.remove(nom)
      with open('wish_list.json', 'w') as f:
        json.dump(wish_list, f)
    elif int(choix) == 3:
      print("tous les items sont :")
      for item in wish_list:
        print(item)
    elif int(choix) == 4:
      run = False
  else:
    print("Veuillez taper un nombre valide")
    pass