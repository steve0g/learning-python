"""
Vérifie si l'adresse IP saisie par l'utilisateur est autorisée.
Demande en boucle à l'utilisateur d'entrer une adresse IP.
Si l'adresse correspond à l'IP autorisée (192.168.1.1),
l'accès est accordé et la boucle se termine.
Sinon, l'accès est refusé et la saisie recommence.
"""

ip_autorisee = "192.168.1.1"
while True:
    adresse_ip = input("Entrer une adresse IP: ")
    if adresse_ip == ip_autorisee:
        print("✅ Accès autorisé au serveur")
        break
    else:
        print("❌ Accès refusé : IP non reconnue")