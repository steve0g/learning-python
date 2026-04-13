"""
Création, ajout dynamique et lecture ciblée dans une liste avec ajout: .append(), Talle: len() et Index: [n]
"""
# Initialisation
nodes = ["Ethereum", "Bitcoin", "Solana"]

# Ajout du reseau Polygon
nodes.append("Polygon")

# Calcule du nombre total d'éléments dans la liste.
total_nodes = len(nodes)

# Affichage du premier et du dernier (avec l'astuce du -1)
print(f"Premier élément : {nodes[0]}")
print(f"Dernier élément : {nodes[-1]}")

# Affichage final
print(f"Liste complète : {nodes}")
print(f"Variable total_nodes : {total_nodes}")