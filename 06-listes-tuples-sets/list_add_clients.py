"""
Ajout d'éléments dans une liste

Description :
    Cet exercice illustre comment construire une liste dynamiquement
    en y ajoutant des éléments un par un en Python.

Objectifs :
    - Créer une liste vide
    - Ajouter des éléments à la liste
    - Afficher la liste finale

Notions abordées :
    - Création d'une liste vide : liste = []
    - Méthode append() pour ajouter un élément à la fin
    - Méthode extend() pour ajouter plusieurs éléments d'un coup
"""

clients = []
clients.append("Stéphane")
clients.append("Obed")
clients.append("Elon")
# # Ajout d'un seul coup avec la methode extend
# clients.extend(["Stéphane", "Obed", "Elon"])
print(clients)