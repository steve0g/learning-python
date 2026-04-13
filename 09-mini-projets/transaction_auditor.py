"""
OBJECTIF : Créer un pipeline de traitement de données (nettoyage, filtrage, alerte).
NOTIONS : Utilisation combinée de map, zip, filter et des générateurs.
DESCRIPTION : 
    Ce script simule l'audit d'un flux de transactions. Il nettoie les noms, 
    élimine les erreurs et surveille les montants importants sans saturer la RAM.
"""

# Données brutes (désordonnées)
users = ["  Alice  ", "Bob", "  Charlie  ", "SpamBot"]
amounts = [1500, -20, 800, 0]

# Nettoyer les pseudos
clean_users = [u.strip() for u in users]
print(clean_users)

# Créer une nouvelle liste qui contient uniquement les transactions ou le montant est positif
valid_transactions = list(filter(lambda x: x[1] > 0, zip(clean_users, amounts)))
print(valid_transactions)

# Afficher une alerte que pour les montants > 1000
alertes = (f"ALERTE : {couple[0]} a envoyé {couple[1]}" for couple in valid_transactions if couple[1] > 1000)

for message in alertes:
    print(message)


