"""
SIMULATEUR DE PARE-FEU (FIREWALL)
---------------------------------
Objectif : Parcourir une série d'identifiants de connexion et bloquer un accès spécifique.
Concepts : Boucle for, range, structures conditionnelles (if/else).
"""

for identifiant in range(1, 11):
    if identifiant == 5:
        print(f"Tentative {identifiant} : ACCÈS BLOQUÉ (IP suspecte)")
    elif identifiant == 8:
        print(f"Tentative {identifiant} : INSPECTION REQUISE")
    else:
        print(f"Tentative {identifiant} : ACCÈS AUTORISÉ")

