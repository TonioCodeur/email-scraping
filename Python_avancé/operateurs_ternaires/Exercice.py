"""En fonction de la valeur de la variable
âge, récupérer grâce à un operateur ternaire
si la personne est majeure ou non dans la variable
'majeur'.
Si la personne est majeur, la variable
contiendra la chaîne de caractère 'majeur'.
Si la personne est mineur, la variable
contiendra la chaîne de caractère 'mineur'"""
age = 17
majeur = "majeur" if age >= 18 else "mineur"
print(f"L'utilisateur d'âge {age} est {majeur}")


"""Récupérer dans la variable extension le mot 'python'
si le fichier déclaré dans la variable 'fichier' est de
type Python (extension .py). Si le fichier n'est pas
de type Python, retourner la chaîne de caractère 'invalide'"""
fichier = 'C:/Python/mon_script.py'
extension = "python" if fichier.endswith(".py") else "invalide"
print(f'Le fichier {fichier} est de type {extension}')

