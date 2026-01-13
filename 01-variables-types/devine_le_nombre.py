# Devine le nombre
nombre_secret = 10

# Demande à l'utilisateur d'entrer un nombre
nombre = int(input("Devine le nombre secret: "))

# Vérification de la réponse
if nombre == nombre_secret:
    print("Bravo ! Tu as trouvé le nombre.")
elif nombre > nombre_secret:
    print("Trop grand")
else:
    print("Trop petit")