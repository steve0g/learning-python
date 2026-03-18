"""
Modification d'un élément dans une liste

Description :
    Cet exercice illustre comment modifier un élément existant
    dans une liste Python en utilisant l'indexation.

Objectifs :
    - Accéder à un élément par son index
    - Modifier sa valeur
    - Afficher la liste mise à jour

Notions abordées :
    - Indexation de liste : liste[index] = nouvelle_valeur
    - Méthode index() pour retrouver la position d'un élément
"""

clients = ["Stéphane", "Obed", "Elon"]
clients[0] = "Maria" 
# Modififation via l'index
# i = clients.index("Elon")
# clients[i] = "Maria"
print(clients)