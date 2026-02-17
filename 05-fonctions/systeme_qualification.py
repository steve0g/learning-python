"""
Système de Qualification
-------------------------------
Ce programme attribue un niveau d'accès selon un score d'examen.
"""

def attribuer_grade(score):
    if score >= 90:
        return "Expert"
    elif score >= 70 and score <= 89:
        return "Confirmé"
    else:
        return "Débutant"

# ---- Programme Principal ----
while True:
    try :
        # Demander le score (int)
        score = int(input("Quel est le score ? "))

        # 🔒 Vérification du score
        if score < 0 or score > 100:
            print("❌ Erreur : le score doit être entre 0 et 100.")
            continue # on redemande

        # Appel de a fonction
        grade = attribuer_grade(score)

        print(f"Félicitation, votre grade est : {score}")
        break

    except ValueError:
        print("❌ Erreur : Merci de saisir un nombre entier.")