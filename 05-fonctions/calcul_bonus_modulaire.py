""" SYSTÈME DE CALCUL DE BONUS MODULAIRE """

def attribuer_grade(score):
    if score >= 90:
        return "Expert"
    elif score >= 70 and score <= 89:
        return "Confirmé"
    else:
        return "Débutant"


def calculer_bonus(score, salaire):
    grade = attribuer_grade(score) # On récupère le grade

    if grade == "Expert":
        return salaire * 0.20
    elif grade == "Confirmé":
        return salaire * 0.10
    else:
        return 0 # Si ce n'est ni Expert ni Confirmé, on renvoie 0

# ---- Programme Principal ----

while True:
    try:
        score = int(input("Quel est le Score ? "))
        salaire = int(input("Quel est le Salaire ? "))
        bonus = calculer_bonus(score, salaire)
        print(f"Le montant du bonus final est {bonus}.")
        print(f"Donc le salaire final est de : {salaire + bonus}. ")
        break

    except ValueError:
        print("ERREUR: Veuillez entrer un nombre entier valide.")