"""
AJOUT DE NUMÉROS UNIQUES DANS UN SET - V1.0
--------------------------------------------
Ce script illustre les concepts fondamentaux suivants :
- Création d'un set vide.
- Ajout d'éléments avec add().
- Comportement d'un set : pas de doublons.
"""

numeros = set()

numeros.add("01")
numeros.add("02")
numeros.add("02")
numeros.add("03")
numeros.add("01")
print(numeros)