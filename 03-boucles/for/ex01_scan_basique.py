"""
SCANNER DE PORTS (BASIQUE)
--------------------------
Objectif : Parcourir une plage de ports définie à l'aide de la fonction range().
Concepts : Boucle for, itération sur une séquence, f-strings.
"""

# Crée une boucle for qui utilise range pour aller de 1 à 15
for port in range (1, 16):
    print(f"Scan du port numéro {port}...")

print("Fin du scan.")