""" Exercice 1 : Variables Numériques et Précision
Dans la finance décentralisée (DeFi), on utilise souvent de très grands nombres entiers pour éviter les erreurs d'arrondi des nombres décimaux (float).

Mission : Gérer un Solde en Wei et des Frais

Créez les variables suivantes et effectuez les calculs :

Déclaration des variables :

solde_initial_wei: Définissez une variable pour le solde initial d'un jeton (utilisez le nombre entier 5 x 10^18 ou 5000000000000000000).

montant_retrait_wei: Définissez une variable pour un retrait (utilisez 1 x 10^18 ou 1000000000000000000).

frais_pourcentage: Définissez une variable pour les frais de protocole (utilisez le nombre décimal 0.005 pour 0.5%).

Calculs : 

Créez une variable frais_totaux_wei qui calcule les frais de protocole sur le montant_retrait_wei. 
Multipliez le montant par le pourcentage. 
(Note : Le résultat sera probablement un float. Gardez-le ainsi pour l'instant.)

Créez une variable montant_net_retire_wei qui calcule le montant retiré après déduction des frais.

Affichage :

Affichez le solde_initial_wei et le montant_net_retire_wei."""

# # Déclaration des variables
solde_initial_wei = 5000000000000000000
montant_retrait_wei = 1000000000000000000
frais_pourcentage = 0.005

# # Calculs des frais
frais_totaux_wei = montant_retrait_wei * frais_pourcentage
print(frais_totaux_wei)

# # Créez une variable montant_net_retire_wei qui calcule le montant retiré après déduction des frais: En gros calcul du montant net retiré
montant_net_retire_wei = montant_retrait_wei - frais_totaux_wei

print(solde_initial_wei)
print(montant_net_retire_wei)

"""✏️ Exercice 1 — Déclarer des variables

Crée les variables suivantes :

age = 35
temperature = 28.7
nombre_etudiants = 150

Ensuite affiche-les avec print()."""

age = 35
temperature = 28.7
nombre_etudiants = 150
print(age)
print(temperature)
print(nombre_etudiants)

"""✏️ Exercice 2 — Opérations simples

Écris un programme qui :

Stocke 10 dans a
Stocke 3 dans b

Affiche :

la somme
la différence
le produit
le quotient
le reste (modulo)
la puissance a élevé à b"""

a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ^ b)

"""✏️ Exercice 3 — Calcul réel

Calcule et affiche le coût total d’un repas :

prix du plat : 2500

prix de la boisson : 800

TVA 18%

Affiche la facture :

Total HT, TVA, Total TTC"""
prix_du_plat = 2500
prix_de_la_boisson = 800
tva = 0.18 # 18%

# # Calculs
total_ht = prix_du_plat + prix_de_la_boisson
montant_tva = total_ht * tva
total_ttc = total_ht + montant_tva

# # Afficher la facture
print("\n---Facture---\n")
print("Total HT = ",total_ht)
print("TVA = ", montant_tva)
print("Total TTC = ", total_ttc)


"""🔥 Exercice suivant (Variables numériques) : Le Convertisseur de Temps

Crée un programme qui :
Demande à l’utilisateur un nombre de secondes (entier).

Convertit ce nombre en :

heures
minutes
secondes restantes

🔍 Rappels utiles :

1 minute = 60 secondes
1 heure = 3600 secondes

🎯 Objectif :

À partir d’un nombre donné (par ex. 10 000 secondes), ton programme doit afficher :

Heures : X
Minutes : Y
Secondes : Z

⚠️ Contraintes :

Utilise des variables numériques uniquement (int, division, modulo).
Pas de fonctions – du code simple.

Tu dois utiliser :
// (division entière)
% (modulo)"""


# Demande à l’utilisateur un nombre de secondes (entier).
total_secondes = int(input("Peux-tu me donner un nombre de secondes ?"))

# Constantes - Valeur qui reste toujours la même
une_heure = 3600
une_minute = 60

# Calcul des heures
heures =  total_secondes // une_heure

# Secondes restantes après les heures
reste = total_secondes % une_heure

# Calculs des minutes
minutes = reste // une_minute

# Calculs des secondes restantes
secondes_restantes = reste % une_minute

# Affichage des heures, minutes et secondes
print("Heures : ", heures)
print("Minutes : ", minutes)
print("Secondes restantes : ", secondes_restantes)

""" Dans ce type d'exercices voici la 
📌 RÈGLE MENTALE À MÉMORISER (à écrire quelque part)
Toujours convertir du plus grand vers le plus petit, en prenant ce qu’on peut (//), puis en continuant avec ce qui reste (%). 

🧠 LA RÈGLE MENTALE À RETENIR (TRÈS IMPORTANTE)
Le modulo (%) s’applique TOUJOURS au nombre initial, jamais au résultat. """