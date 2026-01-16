# EXERCICE 4 — Saisie numérique sécurisée
# Objectif : Demande un nombre entier à l’utilisateur jusqu’à ce qu’il en entre un valide.
# Objectif : Objectif : Empêcher le programme de "crash" si l'utilisateur saisit n'importe quoi.

nombre = ""
while True :
    try:
        nombre = int(input("Veuillez entrer un nombre SVP : "))
        break  # Sort de la boucle si la conversion est réussie
    except ValueError:
        print("Erreur : Ce n'est pas un nombre entier valide. Veuillez réessayer.")
print(f"Merci ! Vous avez entré le nombre entier : {nombre}") 