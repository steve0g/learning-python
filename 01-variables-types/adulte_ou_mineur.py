# Adulte ou mineur
# Demande à l'utilisateur son âge
age_utilisateur = int(input("Entrez votre âge: "))

# Vérification de la réponse
if age_utilisateur < 18:
    print(f"Tu as {age_utilisateur} ans, donc tu es mineur.")
elif age_utilisateur == 18:
    print("Félicitations ! Tu viens d'atteindre la majorité.")
else:
    print(f"Tu as {age_utilisateur} ans, donc tu es majeur.")