"""
SIMULATEUR DE PORTEFEUILLE CRYPTO - V1.0
-----------------------------------------
Ce script illustre les concepts fondamentaux suivants :
- Utilisation d'un set pour la gestion de la whitelist.
- Utilisation d'un dictionnaire pour les soldes des utilisateurs.
- Fonctions de dépôt, retrait et transfert de jetons.
- Vérification des autorisations via la whitelist.
- Boucle de contrôle interactive (menu utilisateur).
- Logique conditionnelle et sécurisation des entrées (try/except).
"""

# La whitelist (set)
whitelist = {"Matthieu", "Marc", "Luc"}

# Le portefeuille (dictionnaire)
crypto_wallet = {
    "Matthieu": 100,
    "Marc": 50,
    "Luc": 0
}

# Fonction dépôt
def deposer(wallet, whitelist, utilisateur, montant):
    if utilisateur in whitelist:
        wallet[utilisateur] += montant
        print(f"Dépôt de {montant} jeton(s) effectué avec succès !")
    else:
        print(f"ERREUR, cet utilisateur n'existe pas")

    return wallet


# Fonction retrait
def retirer(wallet, whitelist, utilisateur, montant):
    if utilisateur in whitelist:
            if wallet[utilisateur] < montant:
                print("ERREUR: Solde insuffisant")   
            else:
                wallet[utilisateur] -= montant
                print(f"Retrait de {montant} jeton(s) effectué avec succès !")
    else:
        print(f"ERREUR, cet utilisateur n'existe pas")

    return wallet


# Fonction transferer
def transferer(wallet, whitelist, utilisateur, receveur, montant):
    if utilisateur in whitelist:
        if  wallet[utilisateur] >= montant:
            wallet[utilisateur] -= montant
            wallet[receveur] += montant
            print(f"Succès : {montant} jetons transférés de {utilisateur} à {receveur}")
        else:
            print("ERREUR: Solde insuffisant")
    else:
        print(f"ERREUR, cet utilisateur n'existe pas")
    
    return wallet
   

# Fonction affichage et Parcours du dictionnaire
def afficher_soldes(wallet):
    for nom, solde in wallet.items():
        print(f"L'utilisateur {nom} possède {solde} jeton(s)")

        if solde == 0:
            print(f"Attention: {nom} est fauché !")


print("-" * 30)

while True:
    try:
        print("\n--- BIENVENUE À LA CRYPTO BANK ---")
        print("1. Déposer des jetons")
        print("2. Retirer des jetons")
        print("3. Transférer des jetons")
        print("4. Afficher les soldes")
        print("5. Quitter")

        choix = int(input("Veuillez choisir une option (1, 2, 3, 4 ou 5)"))

        if choix == 1:
            utilisateur = input("Veuillez entrer votre nom: ")
            montant = int(input("Entrez le montant de dépôt: "))
            deposer(crypto_wallet, whitelist, utilisateur, montant)
        
        elif choix == 2:
            utilisateur = input("Veuillez entrer votre nom: ")
            montant = int(input("Entrez le montant de retrait: "))
            retirer(crypto_wallet, whitelist, utilisateur, montant)

        elif choix == 3:
            utilisateur = input("Veuillez entrer votre nom: ")
            receveur = input("Veuillez entrer votre nom: ")
            montant = int(input("Entrez le montant à transférer: "))
            transferer(crypto_wallet, whitelist, utilisateur, receveur, montant)
        
        elif choix == 4:
            afficher_soldes(crypto_wallet)

        elif choix == 5:
            (print("Merci d'avoir utilisé nos services. Aurevoir et à bientôt..."))
            break

        else:
            print("Erreur, veuillez faire un choix valide. Par exemple : 1, 2, 3, 4 ou 5.")

    except ValueError:
        print("Erreur, veuillez entrer un chiffre valide.")