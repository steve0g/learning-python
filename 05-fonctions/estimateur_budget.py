"""
estimateur_budget.py

Ce programme estime le coût d'une mission d'audit en cybersécurité.
Il demande à l'utilisateur :
- le nombre d'experts
- le nombre de jours

Puis il calcule le coût total en utilisant un tarif de 500€ par jour et par expert.
"""

# Définition de la fonction
def estimer_cout_mission(nb_experts, jours):
    tarif = 500
    total = nb_experts * jours * tarif
    return total

# ---- Le programme principal ----
try :
    nb_experts = int(input("De combien d'expert avez-vous besoin ? "))
    jours = int(input("Pour combien de jours ? "))

    # Appel de la fonction et affichage
    total = estimer_cout_mission(nb_experts, jours)
    print(f"Le prix de la mission d'audit sera de : {total} €")

except ValueError:
    print("❌ Erreur : Veuillez saisir un nombre valide. Exemple : 12")
