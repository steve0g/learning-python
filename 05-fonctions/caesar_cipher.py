"""
CHIFFREMENT DE CÉSAR - V1.0
----------------------------
Ce script illustre les concepts fondamentaux suivants :
- Chiffrement et déchiffrement d'un texte avec le chiffre de César.
- Validation des entrées avec isinstance() et conditions de bornes.
- Manipulation de chaînes de caractères avec maketrans() et translate().
- Utilisation d'un paramètre booléen pour inverser le comportement.

Principe :
- Chaque lettre est décalée de N positions dans l'alphabet.
- Exemple : 'A' avec un décalage de 3 → 'D'
- Pour déchiffrer, on applique le décalage inverse.

Exemple :
- Texte : "Courage" | Décalage : 13 → "Pbhentr"
- Texte : "Pbhentr" | Décalage : 13 → "Courage"
"""

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)