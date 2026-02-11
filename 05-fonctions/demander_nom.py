"""
VALIDATION DE SAISIE DE NOM
Ce script permet de demander et valider le nom d'un utilisateur.
La fonction refuse les réponses vides et redemande jusqu'à obtenir une saisie valide.
"""

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


# Appel de la fonction demander_nom
nom = demander_nom()

print(f"Vous vous appelez {nom}.")