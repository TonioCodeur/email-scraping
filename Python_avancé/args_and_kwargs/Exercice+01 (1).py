def concatenation_chemin(*args):
	return "/".join(args)

chemin_complet = concatenation_chemin('C:/Utilisateurs', 'ThibH', 'Images')
print(chemin_complet)