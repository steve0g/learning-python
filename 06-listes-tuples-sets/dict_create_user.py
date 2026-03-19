"""
CRÉATION D'UN DICTIONNAIRE UTILISATEUR - V1.0
---------------------------------------------
Ce script illustre les concepts fondamentaux suivants :
- Création d'un dictionnaire vide.
- Saisie des données utilisateur via input().
- Ajout dynamique de clés et valeurs dans un dictionnaire.
- Affichage du dictionnaire final.
"""

# Création d'un dictionnaire vide.
user = {}

# Ajout de clés et valeurs dans un dictionnaire en demandant à l'utilisateur 
user["Nom"] = input("Entrez votre nom : ")
user["Age"] = int(input("Entrez votre age : "))
user["Ville"] = input("Entrez votre ville : ")

# Affichage du dictionnaire final.
print(user)