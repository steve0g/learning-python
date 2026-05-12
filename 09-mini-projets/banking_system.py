"""
SYSTÈME DE GESTION BANCAIRE SÉCURISÉ (POO FONDAMENTALE)
------------------------------------------------------
Ce module implémente les concepts clés de la programmation orientée objet :
- Encapsulation : Protection du solde via @property et setters.
- Héritage : Extension des fonctionnalités avec la classe CompteEpargne.
- Abstraction : Validation des entrées (montants positifs, limites de retrait).
- Super() : Délégation de la logique métier à la classe parente.
"""

class CompteBancaire:
    """Compte bancaire de base avec solde sécurisé via encapsulation."""
    def __init__(self, titulaire, solde_initial):
        self.titulaire = titulaire
        self.solde = solde_initial

    # getter pour la lecture sécurisée
    @property
    def solde(self):
        return self.__solde
    
    # setter pour l'écriture sécurisée
    @solde.setter
    def solde(self, solde):
        if solde >= 0:
            self.__solde = solde
        else:
            raise ValueError("Solde négatif interdit")
        
    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif !")
        else:
            self.solde += montant

    def afficher_solde(self):
        print(f"Titulaire: {self.titulaire} | Solde actuel: {self.solde} €")

    def retirer(self, montant):
        if montant < 0:
            raise ValueError("On ne retire pas un montant négatif")
        elif montant > self.solde:
            raise ValueError("Désolé votre solde est insuffisant !")
        else:
            self.solde -= montant

class CompteEpargne(CompteBancaire):
    """Compte épargne avec taux d'intérêt et limite de retrait."""
    def __init__(self, titulaire, solde_initial, taux):
        # On demande au parent de gérer le titulaire et le solde
        super().__init__(titulaire, solde_initial)
        # On gère le nouveau paramètre spécifique à l'enfant ici
        self.taux = taux
        
    def calculer_interets(self):
        interets = self.solde * (self.taux / 100)
        self.deposer(interets)
        print(f"Intérêts ajoutés : {interets}€")

    def retirer(self, montant):
        if montant > 200:
            raise ValueError("Retrait limité à 200€ maximum !")
        super().retirer(montant)

class CompteCrypto(CompteBancaire):
    """Compte crypto avec frais de réseau de 2% sur chaque dépôt."""
    def afficher_solde(self):
        print(f"Crypto Wallet | Titulaire: {self.titulaire} | Solde: {self.solde} ETH")

    def deposer(self, montant):
        frais = montant * (2/100)
        montant_net = montant - frais
        super().deposer(montant_net)
        print(f"Frais de réseau appliqués : {frais} ETH")


def faire_un_don(compte, montant):
    """Dépose un montant sur le compte d'un bénéficiaire."""
    compte.deposer(montant)

        

# --- Exécution (tests) ---

if __name__ == "__main__":

    # --- Phase 1 : Compte bancaire classique ---
    print("\n--- Phase 1 : Compte Bancaire (Marc) ---")
    compte_marc = CompteBancaire("Marc", 100)
    compte_marc.deposer(50)
    compte_marc.afficher_solde()

    try:
        compte_marc.retirer(500)
    except ValueError as e:
        print(f"Sécurité retrait : {e}")

    # Ce qu'on veut tester :
    # Créer un compte épargne
    # Tester la limite de retrait à 200€
    # Faire un retrait valide
    # Calculer les intérêts
    # Afficher le solde final

    # --- Phase 2 : Compte épargne ---
    print("\n--- Phase 2 : Compte Epargne (Steve) ---")
    mon_epargne = CompteEpargne("Steve", 1000, 3)

    try:
        mon_epargne.retirer(500)
    except ValueError as e:
        print(f"Sécurité retrait : {e}")

    mon_epargne.retirer(150)
    mon_epargne.calculer_interets()
    mon_epargne.afficher_solde()

    # Ce qu'on veut tester :
    # Faire un don de Marc vers le compte de Steve
    # Afficher le solde de Steve avant et après

    # --- Phase 3 : Don ---
    print("\n--- Phase 3 : Don (Marc vers Steve) ---")
    print(f"Solde Steve avant don : {mon_epargne.solde} €")
    faire_un_don(mon_epargne, 100)
    print(f"Solde Steve après don : {mon_epargne.solde} €")


    # Ce qu'on veut tester :
    # Créer un compte crypto
    # Déposer des ETH avec les frais de réseau de 2%
    # Afficher le solde

    # --- Phase 4 : Compte Crypto ---
    print("\n--- Phase 4 : Compte Crypto (Gnak) ---")
    compte_crypto = CompteCrypto("Gnak", 10)
    compte_crypto.deposer(5)
    compte_crypto.afficher_solde()


    # Ce qu'on veut tester :
    # Afficher tous les comptes dans une seule boucle
    # Montrer que afficher_solde() s'adapte selon le type d'objet

    # --- Phase 5 : Rapport d'audit ---
    print("\n" + "="*40)
    print("      RAPPORT D'AUDIT (Polymorphisme)")
    print("="*40)

    audit = [compte_marc, mon_epargne, compte_crypto]

    for compte in audit:
        compte.afficher_solde()

    print("="*40)

# if __name__ == "__main__":
    
#     # ENCAPSULATION & ABSTRACTION:
#     # On crée un objet et on manipule ses données via des méthodes sécurisées.
#     # L'utilisateur n'a pas besoin de savoir comment le solde est stocké.

#     print("\n--- Phase 1 : Test Encapsulation (Marc) ---")
#     compte_marc = CompteBancaire("Marc", 100)
#     compte_marc.deposer(50)

#     # L'appel à afficher_solde() utilise le getter sécurisé
#     compte_marc.afficher_solde()

#     # HÉRITAGE (ET EXTENSION): CompteEpargne récupère tout du parent et ajoute ses propres règles.

#     print("\n--- Phase 2: Test Héritage & Super() (Steve) ---")
#     mon_epargne = CompteEpargne("Steve", 1000, 3)

#     # On teste la sécurité (On retire 500 alors que la limite est 200)
#     try:
#         print("Tentative de retrait de 500€ ...")
#         mon_epargne.retirer(500)
#     except ValueError as e:
#         print(f"Sécurité : {e}")

#     # Utilisation d'une méthode spécifique à l'enfant
#     mon_epargne.retirer(150)
#     mon_epargne.calculer_interets()
#     mon_epargne.afficher_solde()

#     """POLYMORPHISME: On traite des objets de types différents via une interface identique."""

#     print("\n" + "="*40)
#     print("    RAPPORT D'AUDIT POLYMORPHE")
#     print("="*40)

#     audit_liste = [
#         CompteBancaire("Marc", 100),        # Objet CompteBancaire
#         CompteEpargne("Steve", 1000, 3),    # Objet CompteEpargne
#         CompteCrypto("Gnak", 10)            # Objet CompteCrypto
#     ]

#     for compte in audit_liste:
#         compte.afficher_solde()

#     print("="*40)

#     print(compte_marc.afficher_solde)
#     compte_marc.afficher_solde()