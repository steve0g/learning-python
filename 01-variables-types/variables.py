# 1er Exo: Création et affichage de variables

# Je vais créer une variable et lui attribuer mon prénom
prenom = "Stephane"
# Je vais afficher un message incluant la variable
print(f"Bonjour {prenom} !")

print("Bonjour ")


# 2eme Exo: Opérations mathématiques avec des variables
# Je vais déclarer 2 variables et leur assigner des valeurs numériques
a = 6
b = 3
# Je vais calculer et afficher leur somme
print(f"Somme = {a + b}")

# Je vais calculer et afficher leur Différence
print(f"Difference = {a - b}")

# Je vais calculer et afficher leur Produit
print(f"Produit = {a * b}")

# Je vais calculer et afficher leur Quotient
print(f"Quotient = {a / b}")

# 3eme Exo: Type de données
# Je declare la variable contenant un nombre entier ou (int).
a = 9
# Je declare la variable contenant un nombre décimal ou (float).
b = 1.5
# Je declare la variable contenant une chaîne de caractères ou (str).
c = "Alvin et Elon sont mes fils"
type(a)
type(b)
type(c)

# 4eme Exo: Demander une entrée utilisateur

# Demande le prénom de l'utilisateur
prenom = input("Quel est ton prenom ?")

# Affiche un message de bienvenue
print(f"Bienvenue {prenom} !")

# 5eme Exo : Conversion de types

# Demande à l'utilisateur un nombre entier
nombre_entier = input("Donne moi un nombre entier et je te donnerai son double :")

# Utilisation de la fonction int() pour transformer la chaîne de caractères en nombre entier.
nombre_entier = int(input("Donne moi un nombre entier et je te donnerai son double :"))

# Calculer le double
double = nombre_entier * 2

# Afficher le double de ce nombre
print(f"Le double de {nombre_entier} est {double}.")