# EXERCICE 3 — Répéter jusqu’à saisie valide (chaîne non vide)
"""Objectif : Demander à l’utilisateur de saisir une chaîne non vide en utilisant une boucle while 
et comprendre la modification de la condition."""

prenom = ""
while prenom == "":
    prenom = input("Quel est votre prénom ? ")
# print("Bonjour " + prenom + " ! Ravi de faire votre connaissance.")  Utilisation de la concaténation
print(f"Bonjour {prenom} ! Ravi de faire votre connaissance.") # Utilisation des f-strings
