# Exercice 9 : Le Menu Interactif
# Objectif : Créer un menu interactif qui permet à l'utilisateur de choisir une option jusqu'à ce qu'il décide de quitter.

while True:
    try:
        print("\nMenu Interactif :")
        print("1. Dire Bonjour")
        print("2. Afficher l'heure")
        print("3. Quitter")

        choix = int(input("Veuillez choisir une option (1, 2 ou 3) : "))

        if choix == 3:
            print("Au revoir")
            break # Sort de la boucle
        elif choix == 1:
            print("Bonjour")
        elif choix == 2:
            print("C'est l'heure de coder.")
        else:
            print("Choix invalide")
    except ValueError:
        print("ERREUR, veuillez entrer un nombre pour choisir")