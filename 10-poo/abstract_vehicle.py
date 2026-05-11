"""
ABSTRACT VEHICLE SYSTEM - V1.0
--------------------------------
Système de véhicules utilisant une classe abstraite.
Illustre le 4ème pilier de la POO : l'abstraction.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self) -> str:
        ...

    @abstractmethod
    def fuel_type(self) -> str:
        ...

class Car(Vehicle):
    def __init__(self, brand: str):
        self.brand = brand

    def start(self) -> str:
        return f"La voiture {self.brand} démarre son moteur silencieux."
    
    def fuel_type(self) -> str:
        return f"La voiture de marque {self.brand} est électrique et se recharge avec l'électricité et non avec le carburant."

class Motorcycle(Vehicle):
    def __init__(self, brand: str):
        self.brand = brand

    def start(self) -> str:
        return f"La moto {self.brand} démarre avec beaucoup de bruit."
    
    def fuel_type(self) -> str:
        return f"La moto de marque {self.brand} utilise du super comme carburant."

class Truck(Vehicle):
    def __init__(self, brand: str):
        self.brand = brand

    def start(self) -> str:
        return f"Le camion {self.brand} démarre avec un petit peu de bruit."
    
    def fuel_type(self) -> str:
        return f"Le camion de marque {self.brand} utilise du diesel comme carburant."
    

def launch(vehicle: Vehicle) -> None:
    print(vehicle.start())
    print(vehicle.fuel_type())

if __name__ == "__main__":
    fleet = [
        Car("Mercedes"),
        Motorcycle("Yamaha"),
        Truck("DAF"),
        Car("Rolls Royce")
    ]

    for f in fleet:
        launch(f)

