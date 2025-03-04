langages = ["C++", "Java", "Rust", "typescript", "Python"]
print(langages[-3])
for i in range(len(langages)):
    print(langages[i])
liste =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(liste[0:2])
print(liste[:-1])
print(liste[::2])
print(liste[::-1])
print(liste[::len(liste)-1])
print(liste.index(3))
langages.sort()
print(langages)
langages.reverse()
print(langages)
langages.pop(-1)
print(langages)
langages.insert(-1, "Golang")
print(langages)
langage = langages.pop(0)
print(langage)
langages.clear()
print(langages)
phrase = ["Python", "est", "un", "langage", "de", "programmation", "orienté", "objet"]
result = " ".join(phrase)
print(result)
langages_dev = "Python, Java, C++, Rust, Typescript, Golang"
liste_langage = langages_dev.split(", ")
print(langages_dev)
print(liste_langage)
users = ["Antonin", "Nabil", "Aurélia"]
if "Antonin" in users:
    print(users)
    users.remove("Antonin")
    print(users)