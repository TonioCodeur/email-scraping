def addition(a, b):
  return a + b

print(addition(1, 2))

def addition_2(*args):
  return sum(args)

print(addition_2(1, 2, 3, 4, 5))

def guess_list(vip_guess, *args):
  print(f"{vip_guess} eszt un VIP")
  for guess in args:
    print(f"{guess} eszt un guess")

guess_list("John", "Jane", "Jim", "Jill")

def guess_list_2(vip_guess, *args, **kwargs):
  print(f"{vip_guess} eszt un VIP")
  for guess in args:
    print(f"{guess} eszt un guess")

    indesirable_guess = kwargs.get("indesirable_guess", None)
    if indesirable_guess:
      for guess in indesirable_guess:
        print(f"{guess} est un guess indésirable")
    else:
      print("Aucun guess indésirable")

guess_list_2("John", "Jane", "Jim", "Jill", indesirable_guess=["Tom", "Donald", "Dwane", "Philip"])

import os


def chemin(dossier, fichier, extention="txt"):
  return os.path.join(f"{dossier} {fichier}.{extention}")

data = {
  "dossier": "C:/Users/John/Documents",
  "fichier": "tutorial",
  "extention": "py"
}

print(chemin(**data))

data = {"dossier": "C:/Users/John/Documents", "fichier": "tutorial"}

print(chemin(**data))

data = {"dossier": "C:/Users/John/Documents", "fichier": "tutorial", "extention": "py"}

data = {"dossier": "C:/Users/John/Documents", "fichier": "tutorial", "extention": "py"}

print(chemin(**data))