"""
SUPPRESSION D'UNE CLÉ DANS UN DICTIONNAIRE - V1.0
--------------------------------------------------
Ce script illustre les concepts fondamentaux suivants :
- Suppression d'une clé et sa valeur dans un dictionnaire.
- Affichage du dictionnaire mis à jour.
"""

user = {"nom": "Alice", "age": 25, "ville": "Abidjan"}

# Suppression d'une clé et sa valeur dans un dictionnaire
del user["ville"]

# Affichage du dictionnaire mis à jour
print(user)