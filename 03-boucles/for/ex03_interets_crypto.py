"""
CALCULATEUR D'INTÉRÊTS CRYPTO
-----------------------------
Objectif : Simuler la croissance d'un capital sur 5 ans avec un taux de 10% par an.
Concepts : Boucle for, mise à jour de variable, calculs mathématiques.
"""

capital = 1000
for year in range(1, 6):
    capital = capital * 1.10
    print(f" Pour l'année {year}, capital = {round(capital, 2)} ETH.")  # ou print(f" Pour l'année {year}, capital = {capital:.2f} ETH.")