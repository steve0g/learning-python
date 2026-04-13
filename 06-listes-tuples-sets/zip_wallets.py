"""
OBJECTIF : Associer des noms d'utilisateurs à leurs adresses publiques.
MÉCANIQUE : Utilisation de zip() pour créer des paires immuables (tuples).
"""

proprietaires = ["Alice", "Bob"]
clefs_publiques = ["0x123", "0x456"]

for owner, key in zip(proprietaires, clefs_publiques):
    print(f"L'adresse de {owner} est {key}")