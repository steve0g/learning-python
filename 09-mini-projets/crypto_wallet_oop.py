"""
PORTEFEUILLE CRYPTO ORIENTÉ OBJET - V1.0
-----------------------------------------
Ce script illustre les concepts fondamentaux suivants :
- Encapsulation des données avec _ et __.
- Getter et Setter avec @property pour un accès contrôlé.
- Validation des données pour protéger l'intégrité du portefeuille.
- Gestion des erreurs avec raise et des exceptions personnalisées.
"""

class CryptoWallet:
    def __init__(self, proprietaire, solde):
        self.proprietaire = proprietaire
        self._solde = solde

    @property
    def solde(self):
        return self._solde
    
    @solde.setter
    def solde(self, solde):
        if solde < 0:
            raise ValueError("Le solde ne doit pas être négatif")
        self._solde = solde

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif !")
        self.solde += montant
        print(f"Dépôt de {montant} ETH ajouté à votre solde avec succès ! Votre nouveau solde est de {self.solde} ETH")

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif !")
        if montant > self.solde: # Si le montant à retirer est plus grand que ce que j'ai dans mon portefeuille → je bloque
            raise ValueError("Solde insuffisant")
        self.solde -= montant
        print(f"Retrait de {montant} ETH effectué avec succès ! Votre nouveau solde est de {self.solde} ETH")

    def transferer(self, receveur, montant):
            if montant <= 0:
                 raise ValueError("Le montant doit être positif !")
            if montant > self.solde: # Si le montant à retirer est plus grand que ce que j'ai dans mon portefeuille → je bloque
                raise ValueError("Solde insuffisant")
            self.solde -= montant  # retire de l'expéditeur
            receveur.solde += montant  # ajoute au receveur
            print(f"Le montant de {montant} ETH a été transféré avec succès à {receveur.proprietaire}, le nouveau solde est de {self.solde} ETH")

    def __str__(self):
        return f"Wallet de {self.proprietaire} | Solde : {self.solde} ETH"


if __name__ == "__main__":
    # Wallets
    wallets = {
        "Marc": CryptoWallet("Marc", 100),
        "Luc": CryptoWallet("Luc", 200),
        "Jean": CryptoWallet("Jean", 400)
    }
    
    # Demander le nom à l'utilisateur et vérifier s'il existe. Sinon redemander
    while True:
        nom = input("Veuillez entrer votre nom SVP : ")
        if nom in wallets:
            wallet = wallets[nom]
            print(wallet)
            break # On sort de la boucle si le nom est valide / dans la liste
        else:
            print(f"Erreur: {nom} n'existe pas ici ! Réessayez.")


    # Menu interactif
    while True:
        try:
            print(f"\n--- BIENVENUE À LA CRYPTO BANK {nom} !---")
            print("1. Déposer des ETH")
            print("2. Retirer des ETH")
            print("3. Transférer des ETH")
            print("4. Quitter")

            choix = int(input("Choisissez une option : 1, 2, 3 ou 4 "))

            if choix == 1:
                montant = int(input("Entrez le montant à déposer : "))
                wallet.deposer(montant)

            elif choix == 2:
                montant_retrait = int(input("Entrez le montant à retirer : "))
                wallet.retirer(montant_retrait)

            elif choix == 3:
                nom_receveur = input("Entrez le nom du receveur : ")
                if nom_receveur in wallets:
                    
                    montant_transfert = int(input("Entrez le montant à transférer : "))
                    receveur = wallets[nom_receveur]
                    wallet.transferer(receveur, montant_transfert)
                else:
                    print(f"Erreur: {nom_receveur} n'existe pas !") 
                            
            
            elif choix == 4:
                print("Aurevoir, à bientôt !")
                break

            else:
                print("Choix invalide ! Veuillez réessayer.")
            
        except ValueError:
            print("ERREUR: cette entrée est invalide")