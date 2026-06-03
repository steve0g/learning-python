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



# --- Exercice 2 : Restaurant ---

class Chef:
    def __init__(self, name: str, specialty: str):
        self.name = name
        self.specialty = specialty
    
class Plat:
    def __init__(self, name: str, chef_name: str, chef_specialty: str):
        self.name = name
        self.chef = Chef(chef_name, chef_specialty)

    def describe(self) -> str:
        return f"Le plat {self.name} a été préparé par {self.chef.name}, spécialiste en {self.chef.specialty}."
    
plat_1 = Plat("Escalope de dinde", "Obed", "Boucherie")
plat_2 = Plat("Macaron", "Mamichou", "Patisserie")

print(plat_1.describe())
print(plat_2.describe())


# --- Exercice 3 : Library ---

class Auteur:
    def __init__(self, name: str, nationality: str):
        self.name = name
        self.nationality = nationality

class Livre:
    def __init__(self, title: str, year: int, author_name: str, author_nationality: str):
        self.title = title
        self.year = year
        self.auteur = Auteur(author_name, author_nationality)

    def describe(self) -> str:
        return f"{self.title} ({self.year}) écrit par {self.auteur.name} ({self.auteur.nationality})."
    
livres = [
    Livre("Père riche, Père Pauvre", 1999, "Robert", "Américain"),
    Livre("Investir en bourse", 2019, "Tamil", "Français"),
    Livre("Apprendre à coder en python", 2020, "Eric", "Français")
]

for l in livres:
    print(l.describe())


