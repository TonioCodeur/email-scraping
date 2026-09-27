import random


class random_letter:
  def __init__(self, name):
    self.i = 0
    self.max = len(name)
    self.rest_name = list(name)

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.i < self.max:
      letter = self.rest_name.pop(random.randint(0, len(self.rest_name) - 1))
      self.i += 1
      return letter
    else:
      raise StopIteration

name = "Antonin"
random_name = random_letter(name)
for letter in random_name:
  print(letter)