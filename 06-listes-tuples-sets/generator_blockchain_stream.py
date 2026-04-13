"""
OBJECTIF : Créer un flux de données dynamique avec un générateur.
MÉCANIQUE : Utilisation de 'yield' pour produire des valeurs une par une.
INTÉRÊT : Apprendre la gestion efficace de la mémoire (Lazy Evaluation) sans stocker de listes massives.
"""

def block_generator():
    n = 1
    while True:
        yield f"Bloc #{n}"
        n += 1

# Création de l'instance du générateur 
mon_flux = block_generator()

# Consommation du flux via une boucle 
for bloc in mon_flux:
    print(bloc)

    # Condition d'arrêt pour éviter la boucle infinie en local
    if "Bloc #10" in bloc:
        break

