# Ligne vide et concaténation

# Pour l'instant, votre objectif est de lister l'identité d'un seul employé : Jean Dupont (Développeur)
# Objectif :
# Vous allez rajouter une nouvelle variable profession, qui contiendra la valeur "Développeur"
# Vous utiliserez cette nouvelle variable (ainsi que nom et prenom) dans votre code, afin que la sortie du programme soit exactement :

nom = "Dupont"
prenom = "Jean"

# Ajout de la variable profession qui contient la valeur "Développeur"
profession = "Développeur"

# Vous utiliserez cette nouvelle variable (ainsi que nom et prenom) dans votre code, afin que la sortie du programme soit exactement :

# Nom : Dupont
# Prénom : Jean
 
# Identité : Jean Dupont (Développeur)

# Objectif de l'exercice: être capable de rajouter des lignes vide dans l'affichage de sortie et de concaténer des variables de type chaine de caractères.

print("Nom : " + nom )
print("Prénom : " + prenom)
print()
# print("Identité : " + prenom + " " + nom + " (" + profession + ")")
print(f"Identité : {prenom} {nom} ({profession})")


# CODE MAL STRUCTURÉ
montant_jetons = 5000
taux_commission = 0.005
adresse_cible = "0xAbCdEf1234567890"
print("--- Démarrage de la Transaction ---")
print(f"Montant: {montant_jetons}")
print(f"Frais: {taux_commission}")
print(f"Cible: {adresse_cible}")
print("--- Vérification du solde en cours ---")


# CODE BIEN STRUCTURÉ (Bloc 1 : Déclaration des Variables)
montant_jetons = 5000
taux_commission = 0.005
adresse_cible = "0xAbCdEf1234567890"

# (Ligne vide introduite)
print() 

# CODE BIEN STRUCTURÉ (Bloc 2 : Affichage des Paramètres)
print("--- Démarrage de la Transaction ---")
print(f"Montant: {montant_jetons}")
print(f"Frais: {taux_commission}")
print(f"Cible: {adresse_cible}")

# (Ligne vide introduite)
print() 

# CODE BIEN STRUCTURÉ (Bloc 3 : Message de Conclusion)
print("--- Vérification du solde en cours ---")


# Informations à coller (Les variables)
prefixe_log = "[ERREUR CRITIQUE]"
code_log = "0x5463"
message_detail = "Le solde a été mis à jour avant la vérification."

# Votre Tâche 1 : Concaténation par l'opérateur +
log_complet_plus = prefixe_log + " " + code_log + " " + message_detail # Votre code ici (coller les trois variables avec des espaces)

# Votre Tâche 2 : Concaténation par f-string
log_complet_fstring = f"{prefixe_log} {code_log} {message_detail}" # Votre code ici (utiliser un f-string pour créer la même phrase)

# Affichez les deux variables pour vérifier votre travail !
print("\n--- Résultat par Opérateur + ---")
print(log_complet_plus)
print()
print("\n--- Résultat par F-string ---")
print(log_complet_fstring)



# Mission : Formater un Reçu de Transaction
# Créez les variables ci-dessous et utilisez un seul print() avec des f-strings et le caractère \n pour afficher le reçu de manière claire et structurée.

# Variables (Simulent les données de la blockchain)
adresse_expediteur = "0xAAA...1234"
adresse_recepteur = "0xBBB...5678"
montant_wei = 1000000000000000000 # Un nombre entier TRES grand (10^18)
symbole_actif = "USDC"
frais_gas_payes = 0.00018 # Le coût de la transaction

# Votre Tâche : Rédiger un SEUL print() pour obtenir cet affichage EXACT :
# (Une ligne vide)
# --- REÇU DE TRANSACTION ---
# (Une ligne vide)
# Montant : 1000000000000000000 USDC
# De : 0xAAA...1234
# À : 0xBBB...5678
# Frais de Gas : 0.00018
# ---------------------------
print("\n--- REÇU DE TRANSACTION ---\n" 
      f"\nMontant : {montant_wei} {symbole_actif}" 
      f"\nDe : {adresse_expediteur}" 
      f"\nÀ : {adresse_recepteur}" 
      f"\nFrais de Gas : {frais_gas_payes}" 
      "\n---------------------------")