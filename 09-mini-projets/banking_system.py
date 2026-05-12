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

    # --- Phase 3 : Don ---
    print("\n--- Phase 3 : Don (Marc vers Steve) ---")
    print(f"Solde Steve avant don : {mon_epargne.solde} €")
    faire_un_don(mon_epargne, 100)
    print(f"Solde Steve après don : {mon_epargne.solde} €")

    # --- Phase 4 : Compte Crypto ---
    print("\n--- Phase 4 : Compte Crypto (Gnak) ---")
    compte_crypto = CompteCrypto("Gnak", 10)
    compte_crypto.deposer(5)
    compte_crypto.afficher_solde()

    # --- Phase 5 : Rapport d'audit ---
    print("\n" + "="*40)
    print("      RAPPORT D'AUDIT (Polymorphisme)")
    print("="*40)

    audit = [compte_marc, mon_epargne, compte_crypto]

    for compte in audit:
        compte.afficher_solde()

    print("="*40)