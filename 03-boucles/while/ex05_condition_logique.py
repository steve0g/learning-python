# EXERCICE 5 — Condition logique
# Objectif : comprendre une condition plus précise.
""" Consigne : Demande un nombre strictement positif ( > 0 ).
Tant que ce n’est pas le cas, redemande."""

nombre = ""
while nombre == "":
    try:
        nombre = int(input("Veuillez entrer un nombre strictement positif ( > 0 ) : "))
        if nombre <= 0:
            print("Erreur : Le nombre doit être strictement positif. Veuillez réessayer.")
            nombre = ""
    except ValueError:
        print("Erreur : Ce n'est pas un nombre entier valide. Veuillez réessayer.")
print(f"Merci ! Vous avez entré le nombre strictement positif : {nombre}")


""" Variante avec while True et break """

nombre = 0
while True:
    try:
        nombre = int(input("Veuillez entrer un nombre strictement positif ( > 0 ) : "))
        if nombre > 0:
            break  # Sort de la boucle si la condition est satisfaite
        else:
            print("Erreur : Le nombre doit être strictement positif. Veuillez réessayer.")
    except ValueError:
        print("Erreur : Ce n'est pas un nombre entier valide. Veuillez réessayer.")
print(f"Merci ! Vous avez entré le nombre strictement positif : {nombre}")