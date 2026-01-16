# EXERCICE 7 — L'Accumulateur (Somme de 1 à N)
# Objectif : Accumuler des valeurs dans une variable
# Objectif : Demander un nombre n à l'utilisateur et calculer la somme de tous les chiffres de 1 jusqu'à n.

# 1. On demande le nombre en sécurisant l'entrée de l'utilisateur
while True:
    try:
        n = int(input("Veuillez entrer un nombre entier positif N : "))
        if n > 0:
            break  # Sort de la boucle si la condition est satisfaite
        else:
            print("Erreur : Le nombre doit être strictement positif. Veuillez réessayer.")
    except ValueError:
        print("Erreur : Ce n'est pas un nombre entier valide. Veuillez réessayer.")

# 2. Initialisation de l'accumulateur et du compteur
somme = 0
i = 1

# 3. Boucle pour accumuler la somme de 1 à N
while i <= n:
    somme = somme + i
    i = i + 1

# 4. Affichage du résultat
print(f"La somme des nombres de 1 à {n} est : {somme}")