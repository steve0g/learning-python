"""Exercice 3

Demande à l’utilisateur un nombre et affiche :

le type AVANT conversion
le type APRÈS conversion

👉 Utilise type()."""

# # Demande d'un nombre à l'utilisateur
nombre = input("Écris un nombre stp : ")

# # Affichage AVANT conversion
print(type(nombre))

# # Affichage APRES conversion
nombre = int(nombre)
print(type(nombre))

age = int(input("Age ? "))
print(type(age))