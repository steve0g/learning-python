"""
SIMULATEUR DE TERMINAL BANCAIRE (ATM) - V1.0
---------------------------------------------
Ce script intègre l'ensemble des concepts fondamentaux :
- Fonctions avec paramètres et valeurs de retour.
- Gestion d'un état (solde) via des variables.
- Boucle de contrôle interactive (menu utilisateur).
- Logique conditionnelle et sécurisation des entrées (try/except).
"""

def retirer_argent(montant, solde):
    nouveau_solde = solde - montant
    if montant > 0 and montant <= solde:
        return nouveau_solde
    else:
        return None

solde_banque = 500

# ---- Le programme principal ----

while True:
    try:
        print("\n--- BIENVENUE À LA BANQUE PYTHON ---")
        print("1. Consulter le solde")
        print("2. Retirer de l'argent")
        print("3. Quitter")

        choix = int(input("Choisissez une option : "))

        if choix == 1:
            print(f"Votre solde est : {solde_banque} ETH")
        elif choix == 2:
            montant = float(input("Veuillez entrer le montant à retirer : "))
            nouveau_solde = retirer_argent(montant, solde_banque)
            if nouveau_solde is None:
                print("Transaction refusée, votre solde est insuffisant")
            else:
                solde_banque = nouveau_solde

        elif choix == 3:
            print("Merci d'avoir utilisé nos services. Aurevoir et à bientôt...")
            break

        else:
            print("Erreur, veuillez faire un choix valide. Par exemple : 1, 2 ou 3.")

    except ValueError:
        print("Erreur, veuillez entrer un chiffre valide.")