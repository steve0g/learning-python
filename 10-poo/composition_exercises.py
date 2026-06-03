"""
COMPOSITION EXERCISES - V1.0
------------------------------
This module consolidates object composition in Python through
practical exercises. Each class demonstrates the HAS-A relationship
between objects.
"""

class Cartable:
    def __init__(self, couleur: str, marque: str):
        self.couleur = couleur
        self.marque = marque

class Eleve:
    def __init__(self, name: str, cartable_brand: str, cartable_color: str):
        self.name = name
        self.cartable = Cartable(cartable_color, cartable_brand)

    def describe(self) -> str:
        return f"{self.name} a un cartable {self.cartable.marque} de couleur {self.cartable.couleur}"

eleve_1 = Eleve("Steve", "Spider", "Bleu")
eleve_2 = Eleve("obed", "Pat patrouille", "Rouge")

print(eleve_1.describe())
print(eleve_2.describe())