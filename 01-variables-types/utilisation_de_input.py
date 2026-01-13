# Utilisation de input()
# Demande à l'utilisateur d'entrer son prénom et stocke-le dans prenom.
prenom = input("Quel est ton prénom ? ")
# Demande son âge et stocke-le dans age (n'oublie pas de convertir en entier).
age = int(input("Quel est ton âge ? "))
# Affiche un message de bienvenue : "Bonjour [prenom], tu as [age] ans."
print(f"Bonjour {prenom}, tu as {age} ans.")