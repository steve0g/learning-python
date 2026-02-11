"""
VALIDATION DE SAISIE D'ÂGE
Ce script permet de demander et valider l'âge d'un utilisateur.
La fonction gère les erreurs de saisie et refuse les valeurs négatives.
"""

def demander_age():
    age = 0
    while age == 0:
        try:
            age = int(input("Quel est votre âge ? "))
            if age < 0:
                print("L'âge ne peut pas être négatif. Veuillez entrer un âge valide.")
                age = 0  # Réinitialiser l'âge pour continuer la boucle
        except ValueError:
            print("Veuillez entrer un âge valide (un nombre entier).")
    return age


# Appel de la fonction demander_age
age = demander_age()

print(f"Vous avez {age} ans.")