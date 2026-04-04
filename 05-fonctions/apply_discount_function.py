"""
CALCULATEUR DE RÉDUCTION SUR UN PRIX - V1.0
--------------------------------------------
Ce script illustre les concepts fondamentaux suivants :
- Définition d'une fonction avec paramètres et valeurs de retour.
- Validation des types avec isinstance().
- Validation des bornes avec des conditions.
- Calcul d'une réduction en pourcentage.

Formule utilisée :
- Réduction = Prix × (Pourcentage / 100)
- Prix Final = Prix - Réduction

Exemple :
- Prix = 50, Réduction = 20% → Prix Final = 40
"""

def apply_discount(price, discount):
    # Validations de type
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    # Validations de bornes
    elif price <= 0:
        return "The price should be greater than 0"
    elif discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    else:
        # Formule : Prix Final = Prix Initial - (Prix Initial * (Pourcentage / 100))
        # Si price=100 et discount=20 -> 100 * 0.20 = 20
        reduction = price * (discount / 100)
        # Soustraire pour avoir le prix final
        final_price = price - reduction
    return final_price

print(apply_discount(74.5, 20.0))
