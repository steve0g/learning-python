"""
PAYMENT POLYMORPHISM DEMO - V1.0
---------------------------------
Ce script illustre le polymorphisme en Python à travers
un système de paiement multi-canal (Mobile Money, Cash, Crypto).
Une fonction externe checkout() traite n'importe quel type
de paiement grâce à l'héritage et l'override de méthodes.
"""

class Payment:
    def __init__(self, amount: int):
        self.amount = amount

    def process(self) -> str:
        return f"Amount is : {self.amount}"
    
class MobileMoney(Payment):
    def process(self) -> str:
        return f"Le montant de {self.amount} FCFA a été envoyé avec succès !"
    
class CashPayment(Payment):
    def process(self) -> str:
        return f"Le montant de {self.amount} FCFA a été remit en mains propre au vendeur."
    
class CryptoPayment(Payment):
    def process(self) -> str:
        return f"Le paiement de {self.amount} USDT envoyé avec succès !"
    

def checkout(payment: Payment) -> None: 
    """Traite un paiement et affiche la confirmation."""
    print(payment.process())

# Traitement de la liste des transactions
transactions = [
    MobileMoney(5000),
    CashPayment(15000),
    CryptoPayment(10),
    MobileMoney(2500)
]
for payment in transactions:
    checkout(payment)