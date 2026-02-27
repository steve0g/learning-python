# EXERCICE 8 — Sécurité Anti-Brute-Force (3 Essais)
"""Objectif : L'utilisateur doit entrer le bon mot de passe, mais il n'a que 3 chances. 
S'il échoue 3 fois, le système se verrouille."""

secret = "Python123"
mot_de_passe_saisi = ""
tentatives = 0 # Le compteur qui va monter de 1 à chaque erreur

while not mot_de_passe_saisi == secret and tentatives < 3:
    mot_de_passe = input("Veuillez entrer le mot de passe : ")
    if mot_de_passe_saisi != secret:
        tentatives += 1
        print(f"❌ Mot de passe incorrect. Il vous reste {3 - tentatives} essai(s)")

if mot_de_passe_saisi == secret:
    print("✅ Mot de passe correct, vous avez accès au compte !")
else:
    print("🔒 Compte bloqué après 3 tentatives")
