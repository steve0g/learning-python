# Calculatrice simple

# Demande à l'utilisateur d'entrer deux nombres et une opération
nombre1 = int(input("Entrez le premier nombre: "))
nombre2 = int(input("Entrez le deuxième nombre: "))

# Demande l'opération
operation = input("Veuillez choisir une opération (+,-,*,/) : ")

# Vérification et calcul
if operation == "+":
    resultat = nombre1 + nombre2
    print(f"Résultat : {nombre1} + {nombre2} = {resultat}")
elif operation == "-":
    resultat = nombre1 - nombre2
    print(f"Résultat : {nombre1} - {nombre2} = {resultat}")
elif operation == "*":
    resultat = nombre1 * nombre2
    print(f"Résultat : {nombre1} * {nombre2} = {resultat}")
elif operation == "/":
    if nombre2 != 0: # Vérification pour éviter la division par zéro
        resultat = nombre1 / nombre2
        print(f"Résultat : {nombre1} / {nombre2} = {resultat}")
    else:
        print("Erreur, division par 0 impossible")
else:
    print("Opération invalide. Veuillez entrer +, -, * ou /.")
        








# if operation == "+":
    resultat = nombre1 + nombre2
    print(f"Résultat : {nombre1} + {nombre2} = {resultat}")
#elif operation == "-":
#    resultat = nombre1 - nombre2
#    print(f"Résultat : {nombre1} - {nombre2 = {resultat}}")
#elif operation == "*":
#    resultat = nombre1 * nombre2
#    print(f"Résultat: {nombre1} * {nombre2} = {resultat}")
#elif operation == "/":
#    if nombre2 != 0:
#        resultat = nombre1 / nombre2
#        print(f"Résultat: {nombre1} / {nombre2} = {resultat}")
#    else:
#        print("Erreur: division par 0 impossible !")
#else:
#    print("Opération invalide. Veuillez entrer +, -, * ou /.")