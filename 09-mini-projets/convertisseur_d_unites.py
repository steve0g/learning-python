"""
CONVERTISSEUR D'UNITÉS (POUCES / CENTIMÈTRES) - V1.0
-----------------------------------------------------
Ce script illustre les concepts fondamentaux suivants :
- Définition de fonctions avec paramètres et valeurs de retour.
- Interaction avec l'utilisateur via input().
- Boucle de contrôle interactive (menu utilisateur).
- Logique conditionnelle et sécurisation des entrées (try/except).

Formules utilisées :
- 1 pouce = 2.54 cm
- 1 cm   = 0.394 pouces
"""

def converti_pouces_en_cm(pouces):
    return pouces * 2.54

def converti_cm_en_pouces(cm):
    return cm / 2.54

# Demander à l'utilisateur le type de conversion
while True:
    try:
        print("1. Convertir des pouces en cm")
        print("2. Convertir des cm en pouces")
        choix = int(input("Que voulez-vous faire ? (1 ou 2) "))

        # Demander le nombre à convertir
        if choix == 1:
            pouces = float(input("Entrez la valeur en pouces : "))
            print(f"{pouces} pouces = {converti_pouces_en_cm(pouces):.2f} cm") # print(f"{pources} pouces = {round(converti_cm_en_pouces(pouces), 2)} cm")

        elif choix == 2:
            cm = float(input("Entrez la valeur en cm : "))
            print(f"{cm} cm = {converti_cm_en_pouces(cm):.2f} pouces") # print(f"{cm} cm = {round(converti_cm_en_pouces(cm), 2)} pouces")

        else:
            print("Choix inconnu. Choisissez 1 ou 2.")
            continue
            
        # La question n'apparaît qu'une seule fois et seulement si une conversion a eu lieu
        autre_conversion = input("Voulez-vous faire une autre conversion ? (oui/non) : ")
        if autre_conversion.lower() != "oui":
            print("Merci d'avoir utilisé le convertisseur d'unités. Au revoir !")
            break
    except ValueError:
        print("ATTENTION: Veuillez entrer un nombre valide.")
