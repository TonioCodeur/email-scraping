import os
from time import time
from random import randint

cur_dir = os.path.dirname(__file__)
fichier = os.path.join(cur_dir, 'nombres_aleatoires.txt')

a = time()

nombre_aleatoire = []
for i in range(5000000):
	nombre_aleatoire.append(str(randint(0, 9999)))
	nombre_aleatoire.append('\n')

with open(fichier, 'w') as f:
	f.write(''.join(nombre_aleatoire))

b = time()

print(f'Temps d\'execution: {b - a} secondes')
