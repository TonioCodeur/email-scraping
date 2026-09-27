for i in range(5):
  print(i)
for l in "HelloWlord":
  print(l)
for key in [("user_01", "Jeremy"), ("user_02", "John"), ("user_03", "Jane")]:
  print(key)

iterator = iter("My name is Antonin")
print(iterator)
print(iterator.__next__())
print(next(iterator))