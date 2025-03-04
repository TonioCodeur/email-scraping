import random

runing = True
while runing:
  max_number = input("vous voulez deviner un nom aléatoire entre 0 et : ")
  max_try = input("Combient de tentatives maximum voulez vous ? : ")
  if max_number.isdigit() and max_try.isdigit():
    number = random.randint(0, int(max_number))
    for i in range(int(max_try)):
      user_try = input(f"tentative {i+1} : ")
      if not user_try.isdigit():
        user_try = input(f"vous n'avez pas entré que des chiffres recommancez. tentative {i+1} : ")
      if number == int(user_try):
        print(f"Vous avez trouvé le nombre {number} en {i+1} tentatives")
        runing = False
        break
      else:
        if number > int(user_try):
          print(f"Le nombre est plus grand que le nombre que vous avez entré. tentative {i+1} : ")
        else:
          print(f"Le nombre est plus petit que le nombre que vous avez entré. tentative {i+1} : ")
  restart = print("Voulez vous recommencer ? y/n ")
  if restart == "n":
    running = False
  elif restart == "y":
    print("bonne chance")
    runing = True
  else:
    print("impossible de lire la réponse donc le soft va restart")
    running = True