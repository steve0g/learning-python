"""
DÉTECTEUR DE FORCE BRUTE
------------------------
Objectif : Surveiller des tentatives de connexion et bloquer l'accès après un seuil.
Concepts : Boucle for, compteurs, conditions imbriquées, rupture de boucle (break).
"""

tentatives_echouees = 0
for compteur in range(1, 16):
    tentatives_echouees += 1
    if compteur == 3:
        print(f"Tentative {compteur} : Attention, 3 échecs consécutifs.")
    elif compteur == 5:
        print(f"Tentative {compteur} : ALERTE : Compte bloqué pour 24h !")
        break
    else:
        print(f"Tentative {compteur} : Identifiants incorrects.")