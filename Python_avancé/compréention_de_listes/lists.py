my_list = [1, 2, 3, 4, 5]
my_list = [i * 2 for i in my_list]
print(my_list) # le contenu de my_list est multiplié par 2

my_list_2 = [1, 2, 3, 4, 5]
my_list_2 = [i * 2 for i in my_list_2 if i % 2 == 0]
print(my_list_2) # le contenu de my_list_é est multiplié par deux et seul les indoces pairs sont gardés

my_list_3 = [1, 2, 3, 4, 5]
my_list_3 = [i * 2 if i % 2 == 0 else i for i in my_list_3]
print(my_list_3) # seul les indices impair de my_list_3 sont plutipliés pas 2