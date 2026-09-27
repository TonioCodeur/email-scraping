# Map et Filter sont des fonctions qui permettent de transformer et de filtrer des listes.
# Map applique une fonction à chaque élément d'une liste et renvoie une nouvelle liste avec les résultats.
# Filter filtre les éléments d'une liste en fonction d'un critère et renvoie une nouvelle liste avec les éléments qui satisfont le critère.
# map et filter sont des fonction plus très utilisés de nos jours.

my_list = [1, 2, 3, 4, 5]

# Avec map
r = map(lambda x: x*x, my_list)
print(list(r))

# Avec les listes en compréhension
r = [i*i for i in my_list]
print(r)

# Avec filter
r = filter(lambda x: x % 2 == 0, my_list)
print(list(r))

# Avec les listes en compréhension
r = [i for i in my_list if i % 2 == 0]
print(r)
