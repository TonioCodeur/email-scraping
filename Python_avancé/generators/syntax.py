def exemple_generator():
  yield 1
  yield 2
  yield 3

gen = exemple_generator()
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))