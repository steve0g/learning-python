"""
Validateur de paiement
Gère les transactions avec vérification du solde et gestion des erreurs.
"""

while True:
    try:
        solde_utilisateur = float(input("Veuillez entrer votre solde : "))
        montant_utilisateur = float(input("Veuillez entrer le montant à envoyer : "))
        if montant_utilisateur > solde_utilisateur:
            print("Transaction refusée : Solde insuffisant.")
        elif montant_utilisateur <= 0:
            print("Erreur : Le montant doit être positif.")
        else:
            nouveau_solde = solde_utilisateur - montant_utilisateur
            print(f"Transaction réussie ! Nouveau solde : {nouveau_solde} ETH.")
            break
    except ValueError:
        print("Veuillez entrer un nombre valide SVP")
