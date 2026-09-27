class custom_range:
  def __init__(self, maximum):
    self.i = 0 # si j'écrivai self.i = 1, a = custom_range(10) aurait 9 valeurs, donc de 1 à 9
    self.max = maximum # si j'écrivai maximum + 1, a = custom_range(10) aurait 11 valeurs, donc de 0 à 10

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.i < self.max:
      i = self.i
      self.i += 1
      return i
    else:
      raise StopIteration

a = custom_range(10)
print(a.__next__())
print(a.__next__())
print(next(a))
for i in a:
  print(i)