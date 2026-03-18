"""
Suppression d'un élément dans une liste

Description :
    Cet exercice illustre les différentes façons de supprimer
    un élément dans une liste Python.

Objectifs :
    - Supprimer un élément par sa valeur
    - Supprimer un élément par son index
    - Afficher la liste mise à jour

Notions abordées :
    - Méthode remove() pour supprimer par valeur
    - Méthode pop() pour supprimer par index
    - Instruction del pour supprimer par index
"""

clients = ["Stéphane", "Obed", "Elon"]
clients.remove("Stéphane")
# del clients[0] # Supprime par position
# clients.pop() # Supprime le dernier dans la liste
print(clients)
