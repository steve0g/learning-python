"""
SALUTATEUR PERSONNALISÉ
-----------------------
Une fonction simple pour valider la récupération de données textuelles
et l'affichage formaté (f-strings).
"""

def dire_bonjour(prenom):
    print(f"Bonjour {prenom}")

prenom = input("Quel est votre prénom ? ")
dire_bonjour(prenom)