"""
ABSTRACT DOCUMENT SYSTEM - V1.0
---------------------------------
Système de documents utilisant une classe abstraite.
Illustre le 4ème pilier de la POO : l'abstraction.
"""

from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def generate(self) -> str:
        ...

    @abstractmethod
    def get_type(self) -> str:
        ...

class Invoice(Document):
    def __init__(self, client: str, amount: int):
        self.client = client
        self.amount = amount

    def generate(self) -> str:
        return f"La facture du client {self.client} est de {self.amount} USD."
    
    def get_type(self) -> str:
        return f"Facture au format PDF généré avec succès !"

class Contract(Document):
    def __init__(self, client: str, duration: int):
        self.client = client
        self.duration = duration

    def generate(self) -> str:
        return f"Le contrat du client {self.client} est de {self.duration} mois."
    
    def get_type(self) -> str:
        return f"Contrat généré avec succès ! Type de document : PDF."

class Report(Document):
    def __init__(self, title: str):
        self.title = title

    def generate(self) -> str:
        return f"{self.title}."
    
    def get_type(self) -> str:
        return f"Rapport PDF généré avec succès !"

def print_document(document:  Document) -> None:
    print(document.generate())
    print(document.get_type())


if __name__ == "__main__":
    doc = [
        Invoice("Steve", 1000000),
        Contract("Obed", 12),
        Report("Rapport des prestations"),
        Invoice("Steve", 500000),
    ]

    for d in doc:
        print_document(d)


    