"""
ANALYSEUR DE PARITÉ
-------------------
Objectif : Parcourir des nombres et déterminer s'ils sont pairs ou impairs.
Concepts : Boucle for, opérateur modulo (%), conditions if/else.
"""

for n in range(1, 21):
    if n % 2 == 0: # signifie que le nombre est pair
        print(f"Le nombre {n} est PAIR")
    else:
        print(f"Le nombre {n} est IMPAIR")