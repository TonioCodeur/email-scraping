print("Objets mutables :")
liste = [1, 2, 3]
print(id(liste))
liste.append(4)
print(id(liste))

print("--------------------------------")

print("Objets immuables :")
prenom = 'Pierre'
print(id(prenom))
prenom += ' Dupont'
print(id(prenom))


