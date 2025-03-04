running = True
while running:
  user_size = input("Entrez votre taille en cm ")
  user_wheight = input("Entrez votre poids en Kg ")
  if user_size.isdigit() and user_wheight.isdigit():
    user_size = float(user_size)
    user_wheight = float(user_wheight)
    user_size /= 100
    result = user_wheight / (user_size * user_size)
    result = int(result)
    print(f"votre IMC est de {result}")
    restart = input("Voulez vous calculer un autre IMC ? y/n")
    if restart == "n":
      running = False
  else:
    print("Veuillez à n'entrer que des nombres")
    running = True