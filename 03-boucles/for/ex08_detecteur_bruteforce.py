"""
DÉTECTEUR DE FORCE BRUTE
------------------------
Objectif : Surveiller des tentatives de connexion et bloquer l'accès après un seuil.
           Confirmer l'intégrité du système si aucun blocage n'est survenu.
Concepts : Boucle for, compteurs, rupture de boucle (break), clause de succès (else).
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

# Ce bloc s'exécute UNIQUEMENT si la boucle se termine SANS avoir rencontré de 'break'
# (C'est-à-dire si aucune menace n'a été détectée après les 15 tours)
else:
    print(f"Analyse terminée: Aucune menace critique détectée sur les 15 tentatives.")