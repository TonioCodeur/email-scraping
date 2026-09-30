# fonction custom_range qui renvoie un generator
def custom_range(n):
  for i in range(1, n + 1):
    yield i

generator = custom_range(10)
print(type(generator))
for i in generator:
  print(i)

from random import randint


def random_letter(name):
  name_list = list(name)
  for i in range(len(name)):
    rand_index = randint(0, len(name_list) - 1)
    yield name_list.pop(rand_index)

word = input("Enter a word: ")
for letter in random_letter(word):
  print(letter)
name_shuffle = "".join([letter for letter in random_letter(word)])
print(name_shuffle.capitalize())