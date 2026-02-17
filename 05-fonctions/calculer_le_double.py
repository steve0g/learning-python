"""
CALCULATEUR DE DOUBLE v1.0
--------------------------
Ce script illustre le fonctionnement d'une fonction mathématique simple 
avec une gestion robuste des erreurs de saisie utilisateur via une boucle.
"""

def calculer_le_double(nombre):
    double = 2 * nombre
    return double

# --- UTILISATION ---

while True:
    try:
        nombre = int(input("Entrez un nombre : "))

        resultat = calculer_le_double(nombre)

        print(f"Le double de {nombre} est {resultat}.")
        break

    except ValueError:
        print("❌ Erreur : Veuillez saisir un nombre valide.")