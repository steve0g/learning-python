"""
Vérificateur de force de mot de passe.
"""

while True:
    mot_de_passe = input("Choisissez le mot de passe : ")
    if len(mot_de_passe) < 8:
        print("Trop court ! (Minimum 8 caractères)")
    elif mot_de_passe == "12345678" or mot_de_passe == "password":
        print("Trop commun ! Choisissez un mot de passe plus complexe.")
    else:
        print("Mot de passe valide et sécurisé.")
        break