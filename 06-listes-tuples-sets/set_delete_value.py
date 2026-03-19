"""
SUPPRESSION D'UNE VALEUR DANS UN SET - V1.0
--------------------------------------------
Ce script illustre les concepts fondamentaux suivants :
- Suppression d'un élément avec remove().
- Suppression d'un élément avec discard().
- Différence de comportement entre les deux méthodes.
"""

numeros = {"0702", "0703", "0704"}

# Suppression d'un élément avec remove()
numeros.remove("0702")
print(numeros)

# Suppression d'un élément avec discard()
numeros.discard("0703")
print(numeros)

# Différence de comportement entre les deux méthodes est que discard n'affiche pas d'erreur lorsque l'élément à supprimer n'existe pas mais remove sort une KeyError