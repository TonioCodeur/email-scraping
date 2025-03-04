def chiffrer(texte, mot_de_passe):
    texte_chiffre = ""
    for i, char in enumerate(texte):
        cle = ord(mot_de_passe[i % len(mot_de_passe)])
        texte_chiffre += chr(ord(char) ^ cle)
    return texte_chiffre

def dechiffrer(texte_chiffre, mot_de_passe):
    return chiffrer(texte_chiffre, mot_de_passe)  # Le déchiffrement est identique au chiffrement avec XOR

# Exemple d'utilisation
texte_original = "Bonjour, ceci est un message secret !"
mot_de_passe = "cle_secrete"

texte_chiffre = chiffrer(texte_original, mot_de_passe)
print("Texte chiffré:", texte_chiffre)

texte_dechiffre = dechiffrer(texte_chiffre, mot_de_passe)
print("Texte déchiffré:", texte_dechiffre)