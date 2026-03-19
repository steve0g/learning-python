"""
MODIFICATION D'UN TUPLE VIA CONVERSION - V1.0
---------------------------------------------
Ce script illustre les concepts fondamentaux suivants :
- Conversion d'un tuple en liste pour le modifier.
- Ajout d'un élément dans la liste.
- Reconversion de la liste en tuple.
"""

t = ("Alice", "Marie")

# Conversion d'un tuple en liste pour le modifier
liste = list(t)

# Ajout d'un élément dans la liste.
liste.append("Jean")

# Reconversion de la liste en tuple.
t = tuple(liste)
print(t) 