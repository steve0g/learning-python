"""
PRÉDICTEUR D'ÂGE v1.0
---------------------
Ce script calcule l'âge d'un utilisateur dans une décennie.
Il inclut une validation stricte pour empêcher les âges négatifs 
et les erreurs de type (chaînes de caractères).
"""

def age_dans_10_ans(age):
    return age + 10

# --- UTILISATION ---

while True:
    try:
        age = int(input("Quel est votre âge ? "))
        if age < 0:
            print("L'âge doit être positif")
            continue

        future_age = age_dans_10_ans(age)

        print(f"Dans 10 ans tu auras {future_age} ans.")
        break

    except ValueError:
        print("❌ Erreur : Veuillez saisir un nombre valide et strictement positif.")