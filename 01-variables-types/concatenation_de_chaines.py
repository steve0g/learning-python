# Concaténation de chaînes

# Demande à l’utilisateur de saisir son prénom et son nom.
prenom = input("Quel est votre prénom ?")
nom = input("Quel est votre nom ?")

# Concaténation de chaînes
nom_complet = prenom + " " + nom

# Affichage du message final
# print("Bonjour " + nom_complet + ", bienvenue !")
print(f"Bonjour {prenom} {nom}, bienvenue !") # Utilisation d'une f-string pour l'affichage


