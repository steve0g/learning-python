"""
CALCUL DE PRIX FINAUX AVEC MAP() - V1.0
-----------------------------------------
Ce script illustre les concepts fondamentaux suivants :
- Utilisation de map() pour appliquer une fonction à chaque élément.
- Utilisation de lambda pour définir une fonction anonyme.
- Calcul de prix finaux après application de réductions en pourcentage.

Formule utilisée :
- Prix Final = Prix × (1 - Réduction / 100)

Exemple :
- Prix = 100, Réduction = 10% → Prix Final = 90.0
"""

prix = [100, 50, 200, 75]
reductions = [10, 5, 20, 25]

prix_final = list(map(lambda p, r: p * (1 - r/100), prix, reductions))
print(prix_final)