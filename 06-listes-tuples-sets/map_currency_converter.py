"""
OBJECTIF : Convertir une liste de valeurs ETH en USD de manière massive.
MÉCANIQUE : Utilisation de map() pour appliquer un multiplicateur constant à chaque élément.
"""

prix_eth = [1, 2.5, 0.8]

# Transforme cette liste en prix USD si 1 ETH = 3000 USD.
prix_usd = list(map(lambda x: x * 3000, prix_eth))
print(prix_usd)