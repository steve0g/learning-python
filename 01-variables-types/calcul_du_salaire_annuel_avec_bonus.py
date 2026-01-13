# Exercice : Calcul du salaire annuel avec bonus

# Déclaration des variables
nom = "Kouadio"
salaire_mensuel = 150000
bonus_annuel = 250000

# Calculer le salaire annuel total en tenant compte du bonus.
# Pour le faire on va multiplier la salaire mensuel par 12 et additionner le resultat au bonus_annuel

# Déclaration de la variable nombre_de_mois
nombre_de_mois = 12

# multiplier la salaire mensuel par nombre_de_mois + addition du bonus annuel
print("Nouveau salaire =", int(salaire_mensuel) * int(nombre_de_mois) + int(bonus_annuel))

# Variable Nouveau Salaire
nouveau_salaire = int(salaire_mensuel) * int(nombre_de_mois) + int(bonus_annuel)

# Affichage de la phrase
print(f"{nom} gagne {nouveau_salaire} FCFA par an, bonus compris.")

