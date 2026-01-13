"""Niveau 1 — Conversion directe (bases)
Exercice 1

Demande à l’utilisateur son âge (avec input) et stocke-le dans une variable entière.

👉 Affiche ensuite :

Dans 5 ans, tu auras X ans"""

# Demande de l'âge de l'utilisateur
age = int(input("Quel est ton âge ?"))
age_prochain = age + 5
# print("Dans 5 ans, tu auras " + str(age_prochain) + " ans")
print(f"Dans 5 ans, tu auras {age_prochain} ans")

"""Exercice 2

Demande à l’utilisateur deux nombres sous forme de texte et affiche leur somme.

⚠️ Attention : "10" + "20" ≠ 30"""
nombre_un = input("Affiche un nombre")
nombre_deux = input("Affiche un autre nombre")
nombre = int(nombre_un) + int(nombre_deux)
print(nombre)

# Test push depuis VS Code



