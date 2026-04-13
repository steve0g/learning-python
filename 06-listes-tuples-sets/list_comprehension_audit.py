"""
OBJECTIF : Filtrer et formater des noms d'utilisateurs en une seule ligne.
MÉCANIQUE : Syntaxe [transform for item in list if condition].
"""

users = ["satoshi", "hacker_123", "vitalik", "admin"]

# Créer une nouvelle liste contenant uniquement les pseudos qui commencent par "s" ou "v",
allowed_users = [u.upper() for u in users if u.startswith('s') or u.startswith('v')]
print(allowed_users)

# On rajoute simplement un 'and' à la fin du filtre
allowed_users = [
    u.upper() for u in users
    if u.startswith('s') or u.startswith('v') and len(u) < 8
]
print(allowed_users)