my_set = {1, 2, 3, 3, "Julien", "Julien", (255, 0, 0), (255, 0, 0)}
print(my_set)
my_set.add(5)
my_set.update(["Pièrre", 6])
print(my_set)
my_set.remove("Julien")
print(my_set)
my_set.discard("Jules") # ne provoque pas d'erreurs si l'élément n'existe pas alors que si on utilise remove, il provoque une erreur.

my_list = [99, 46, 46, 51, 48, 51, 99, 20, 20, 20, 20, 1, 18]
print(sorted(set(my_list))) #trie les éléments de la liste et les met dans un set pour enlever les doublons

