"""
DÉTECTION DE VULNÉRABILITÉ
--------------------------
Objectif : Identifier un port spécifique (le port 7) au milieu d'un scan automatique.
Concepts : Boucle for, structures conditionnelles imbriquées (if/else).
"""

for port in range(1, 11):
    if port == 7:
        print(f"Alerte ! Port {port} vulnérable !")
    else:
        print(f"Port {port} : Sécurisé")