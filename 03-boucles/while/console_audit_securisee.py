"""
TERMINAL D'AUDIT SÉCURISÉ v1.0
------------------------------
Description : Interface de gestion pour auditeurs cybersécurité.
Fonctions : Authentification, Scan de serveurs, Estimation budgétaire.


NOTES MÉMO :
- i += 1 : Évite la boucle infinie en faisant avancer le compteur.
- total += 500 : Logique du réservoir (on ajoute au lieu de remplacer).
- break : Bouton d'éjection pour sortir de la boucle True.
"""

# --- ÉTAPE 1 : AUTHENTIFICATION ---

secret = "admin123"
tentatives_max = 3
nombre_essais = 0  # Le compteur qui va monter de 1 à chaque erreur
mot_de_passe_saisi = ""

# La boucle tourne tant que le MDP est faux ET qu'on a encore des essais
while not mot_de_passe_saisi == secret and nombre_essais < tentatives_max:
    mot_de_passe_saisi = input("Veuillez entrer le mot de passe : ")
    if mot_de_passe_saisi != secret:
        nombre_essais += 1 # On incrémente le compteur d'erreurs
        print(f"❌ Mot de passe incorrect. Il vous reste {3 - nombre_essais} essai(s)")

# On vérifie si on est sorti de la boucle parce qu'on a réussi
if mot_de_passe_saisi == secret:
    print("✅ Mot de passe correct, vous avez accès au compte !")

    # --- ÉTAPE 2 : MENU PRINCIPAL ---
    # while True crée une boucle infinie qui ne s'arrête que par un 'break'
    while True:
        print("\n--- CONSOLE D'AUDIT ---")
        print("1. Scan serveurs | 2. Budget | 3. Quitter")

        # --- ÉTAPE 3 : GESTION DES CHOIX ---
        # Utilise try/except pour le choix du menu
        try:
            choix = int(input("Veuillez choisir une option (1, 2 ou 3) : ")) # Conversion forcée en entier

            # --- OPTION 1 : SCAN ---
            if choix == 1:
                nombre_de_serveur = int(input("Combien de serveurs ? : "))
                i = 1  # # Initialisation du compteur de scan
                while i <= nombre_de_serveur:  # Boucle de scan : tant que i n'a pas atteint le nombre demandé
                    print(f"Scan du serveur {i} / {nombre_de_serveur} en cours...")
                    i += 1  # Passage au serveur suivant
                print("✅ Tous les serveurs ont été analysés.")

            # --- OPTION 2 : BUDGET
            elif choix == 2:
                # 1. On demande les jours (avec sécurité)
                nombre_jours_attaque = int(input("Entrez le nombre de jours d'attaque : "))

                # 2. Logique d'accumulation
                total = 0 # Initialisation de l'accumulateur (le panier vide)
                compteur = 1
                while compteur <= nombre_jours_attaque:
                    total += 500  # On ajout 500 à chaque jour (accumulation)
                    print(f"Jour {compteur} : Coût accumulé = {total}€")
                    compteur += 1 # Avancement du temps

                print(f"💰 Budget total estimé : {total}€")

            # --- OPTION 3 : QUITTER ---
            elif choix == 3:
                print("👋 Déconnexion de la console...")
                break  # Arrête la boucle infinie 'while True' et ferme le menu
            else:
                print("⚠️ Choix inconnu. Choisissez 1, 2 ou 3.")

        except ValueError:
            # Gestion du cas où l'utilisateur tape du texte au lieu d'un chiffre
            print("❌ ERREUR: Ceci n'est pas un nombre valide, veuillez entrer un nombre valide SVP")

else:
    # Cas où on est sorti de la boucle car nombre_essais == tentatives_max
    print("🔒 ACCÈS REFUSÉ : Arrêt du système...")