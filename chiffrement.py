def crypt(texte, mot_de_passe):
    texte_chiffre = ""
    for i, char in enumerate(texte):
        cle = ord(mot_de_passe[i % len(mot_de_passe)])
        texte_chiffre += chr(ord(char) ^ cle)
    return texte_chiffre

def deccrypt(texte_chiffre, mot_de_passe):
    return crypt(texte_chiffre, mot_de_passe)  # Le déchiffrement est identique au chiffrement avec XOR

# Exemple d'utilisation
texte_original = "Bonjour, ceci est un message secret !"
mot_de_passe = "cle_secrete"

texte_chiffre = crypt(texte_original, mot_de_passe)
print("Texte chiffré:", texte_chiffre)

texte_dechiffre = deccrypt(texte_chiffre, mot_de_passe)
print("Texte déchiffré:", texte_dechiffre)