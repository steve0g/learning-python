# EXERCICE 6 — Le Signal d'Arrêt (Break)
# Créer une boucle qui demande des mots à l'utilisateur et s'arrête uniquement quand il tape un mot "clé".

mot = ""
while True:
    mot = input("Tapez quelque chose (ou 'stop' pour quitter) : ")
    if mot == "stop":
        break  # Sort de la boucle si l'utilisateur tape "stop"
    else:
        print(f"Vous avez tapé : {mot}")
print("Programme terminé, au revoir !")


""" Variante sans while True et break """

mot = ""
while mot != "stop":
    mot = input("Tapez quelque chose (ou 'stop' pour quitter) : ")
    if mot != "stop":
        print(f"Vous avez tapé : {mot}")
print("Programme terminé, au revoir !")