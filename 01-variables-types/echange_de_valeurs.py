# Échange de valeurs
# Déclare deux variables : x = 3 et y = 7.
x = 3
y = 7
# Échange leurs valeurs sans créer une troisième variable temporaire.
x, y = y, x
# Affiche les nouvelles valeurs de x et y
print("x =", x)
print("y =", y)

# print(f"x = {x}, y = {y}")


# 3️⃣ Échanger deux variables

# Crée deux variables x = 5 et y = 10.
x = 5
y = 10
print("Avant : x =", x, "y =", y)
# Échange leurs valeurs sans utiliser de variable temporaire.
x, y = y, x
print("Après : x =", y, "y =", x)
