import time

my_list = range(100000)

a = time.time()

result= ''
for number in my_list:
  result += str(number)

b = time.time()

print(f"Temps d'exécution : {b - a} secondes")

a = time.time()

result = []
for number in my_list:
  result.append(str(number))

final_result = ''.join(result)

b = time.time()

print(f"Temps d'exécution : {b - a} secondes")