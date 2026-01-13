# Forme complète (if, elif et else)
# Les limites de la condition simple en if

a = 5
if a > 0: # Si a est supérieur a 0
    print("a est positif.")
if a < 0: # Si a est inférieur a 0
    print("a est négatif.")


a = 5
b = 8
if a > 0: # Si a est supérieur a 0
    # On incrémente la valeur de b
    b += 1
    print("a =", a, "et b =", b)


# L’instruction else

# Le mot-clé else, qui signiﬁe « sinon » en anglais, permet de déﬁnir une première forme de complément à notre instruction if.
age = 21
if age >= 18: # Si age est supérieur ou égale à 18
    print("vous êtes majeur.")
else: # Sinon (age est inférieur à 18)
    print("Vous êtes mineur")

# if age < 18: # Si age est inférieur à 18
#    print("Vous êtes mineur.")
#else : # Si age est supérieur à 18
#   print("Vous êtes majeur.")

a = 5
if a > 0:
    print("a est supérieur à 0.")
else:
    print("a est inférieur à 0.")


# L’instruction elif
# Le mot-clé elif est une contraction de « else if », que l’on peut traduire très littéralement par « sinon si ». 
# Dans l’exemple que nous venons juste de voir, l’idéal serait d’écrire 

# — si a est strictement supérieur à 0, on dit qu’il est positif ;
# — sinon si a est strictement inférieur à 0, on dit qu’il est négatif ;
# — sinon, (a ne peut qu’être égal à 0), on dit alors que a est nul.

if a > 0:
    print("a est positif.")
elif a < 0:
    print("a est négatif.")
else:
    print("a est nul.")


