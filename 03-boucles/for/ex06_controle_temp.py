"""
SYSTÈME DE SURVEILLANCE THERMIQUE
---------------------------------
Objectif : Simuler des relevés et déclencher des alertes selon des seuils.
Concepts : Boucle for, conditions multiples (if/elif/else).
"""

temperature = 20
for heure in range(1, 11):
    temperature += 5
    if temperature > 60:
        print(f"Heure {heure} : {temperature}°C - DANGER : Surchauffe !")
    elif temperature > 45:
        print(f"Heure {heure} : {temperature}°C - ATTENTION : Ventilateurs à fond")
    else:
        print(f"Heure {heure} : {temperature}°C - Température stable")