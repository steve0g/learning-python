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

# age = int(input("Age ? "))
print(type(age))

age = age + "5"


# Quel est le problème potentiel dans ce code ?

age = int(input("Age : "))
print(age + 10)

# 👉 Donne 2 saisies utilisateur qui feront planter le programme.

x = input("Nombre : ")
y = int(x)
print(y)