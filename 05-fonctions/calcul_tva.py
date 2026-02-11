"""
UTILITAIRE DE CALCUL DE TAXE
Ce script permet de calculer automatiquement la TVA.
"""

# Fonction qui calcule et renvoie le montant de la TVA (20%)
def calculer_tva(prix_ht):
    montant_tva = 0.20 * prix_ht
    return montant_tva

# --- UTILISATION ---
prix_ht = 1000
ma_tva = calculer_tva(prix_ht)

print(f"Prix HT : {prix_ht}€")
print(f"La TVA pour cet article est de {ma_tva}")