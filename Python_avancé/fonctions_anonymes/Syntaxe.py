def multiplication(a, b):
	return a * b


multiplication = lambda a, b: a * b 
resultat = multiplication(5, 10)
print(resultat)


def print_bonjour():
	print('Bonjour')

print_bonjour()

# Fonctionne uniquement avec Python 3.x !
print_bonjour = lambda: print('Bonjour')
print_bonjour()

print_mot = lambda m: print(m)
print_mot('Udemy')