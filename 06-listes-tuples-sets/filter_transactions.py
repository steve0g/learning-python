"""
OBJECTIF : Isoler les transactions financières réelles des bruits de réseau.
MÉCANIQUE : Utilisation de filter() avec une fonction lambda pour valider les montants > 0.
"""

tx = [500, -10, 0, 1200, -5, 10]

res = list(filter(lambda x: x > 0, tx))
print(res)