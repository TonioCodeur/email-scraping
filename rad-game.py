import random

result = 0
for i in range(1000):
  result += random.randint(-1, 1)
  print(result)