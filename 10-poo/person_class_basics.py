"""
Person class modeling with OOP basics.

Demonstrates instance attributes, methods, and conditional logic
through a simple Person class with self-introduction behavior.
"""

class Personne:
    """
    Represents a person with a name, age, and gender.

    Attributes:
        nom (str): Full name of the person.
        age (int): Age in years.
        genre (bool): True pour Masculin, False pour Féminin.
    """

    def __init__(self, nom: str, age: int, genre: bool) -> None:
        self.nom = nom
        self.age = age
        self.genre = genre

    def is_adult(self) -> bool:
        """Return True if the person is 18 or older."""
        return self.age >= 18
    
    def introduce(self) -> None:
        """Print a self-introduction with gender-appropriate grammar."""
        print(f"Bonjour, je m'appelle {self.nom}, j'ai {self.age} ans")

        if self.genre: 
            print("Genre : Masculin")
            print("Je suis majeur" if self.is_adult() else "Je suis mineur")
        else: 
            print("Genre : Feminin")
            print("Je suis majeure" if self.is_adult() else "Je suis mineure")
        print()

    
if __name__ == "__main__":
    personne1 = Personne("Jean", 25, True)
    personne1.introduce()

    personne2 = Personne("Emilie", 17, False)
    personne2.introduce()