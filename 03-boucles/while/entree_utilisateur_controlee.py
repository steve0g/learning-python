"""Entrée utilisateur contrôlée avec une boucle while et concaténation de chaînes"""

# Demande le nom à l'utilisateur
nom = input("Quel est votre nom ? ")

# Demande l'âge à l'utilisateur avec contrôle de saisie
age = 0
while age == 0:
    age_str = input("Quel est votre âge ? ")
    try:
        age = int(age_str)
    except ValueError:
        print("Veuillez entrer un âge valide (un nombre entier).")

print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
print("L'an prochain vous aurez " + str(age + 1) + " ans.")


"""Essai avec while True et break et f-strings"""

# Demande le nom à l'utilisateur
nom = input("quel est votre nom ? ")

# Demande l'âge à l'utilisateur avec contrôle de saisie
age = 0
while True:
    age_str = input("quel est votre âge ? ")
    try:
        age = int(age_str)
        break # Sort de la boucle si la conversion est réussie
    except ValueError:
        print("Veuillez entrer un âge valide (un nombre entier).")

print(f"Vous vous appelez {nom}, vous avez {age} ans.")
print(f"L'an prochain vous aurez {age + 1} ans ")



"""Essai en simplifiant la conversion de age avec while True et break et f-strings"""

# Demande le nom à l'utilisateur
nom = input("quel est votre nom ? ")

# Demande l'âge à l'utilisateur avec contrôle de saisie
while True:
    try:
        age = int(input("quel est votre âge ? "))
        break # Sort de la boucle si la conversion est réussie
    except ValueError:
        print("Veuillez entrer un âge valide (un nombre entier).")

print(f"Vous vous appelez {nom}, vous avez {age} ans.")
print(f"L'an prochain vous aurez {age + 1} ans ")


"""Essai en simplifiant la conversion de age sans while True et break et f-strings"""

# Demande le nom à l'utilisateur
nom = input("quel est votre nom ? ")

# Demande l'âge à l'utilisateur avec contrôle de saisie
age = 0
while age == 0:
    try:
        age = int(input("quel est votre âge ? "))
    except ValueError:
        print("Veuillez entrer un âge valide (un nombre entier).")

print(f"Vous vous appelez {nom}, vous avez {age} ans.")
print(f"L'an prochain vous aurez {age + 1} ans ")


"""Tester si la variable nom est vide et demander tant que c'est le cas"""
# Demande le nom à l'utilisateur avec contrôle de saisie
nom = ""

while nom == "":
        nom = input("quel est votre nom ? ")

print(f"Bonjour {nom} !")

age = 0
while age == 0:
    try:
        age = int(input("Quel est votre âge ? "))
    except ValueError:
        print("Veuillez entrer un âge valide (un nombre entier).")

print(f"Vous vous appelez {nom}, vous avez {age} ans.")
print(f"L'an prochain vous aurez {age + 1} ans ")
    