"""
ABSTRACT EMPLOYEE SYSTEM - V1.0
---------------------------------
Système de gestion d'employés utilisant une classe abstraite.
Illustre le 4ème pilier de la POO : l'abstraction.
"""

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def get_salary(self) -> str:
        ...

    @abstractmethod
    def get_contract_type(self) -> str:
        ...

    def introduce(self) -> str:
        return f"Je suis {self.name}, employé chez Fluxinnov."
    
class FullTime(Employee):
    def __init__(self, name: str, monthly_salary: int):
        self.name = name
        self.monthly_salary = monthly_salary

    def get_salary(self) -> str:
        return f"Le salaire de {self.name} est de : {self.monthly_salary} USD /mois."
    
    def get_contract_type(self) -> str:
        return f"Type de contrat: Plein temps."
    
class PartTime(Employee):
    def __init__(self, name: str, hourly_rate: int, hours_worked: int):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_salary(self) -> str:
        total = self.hourly_rate * self.hours_worked
        return f"Le salaire de {self.name} est de : {total} USD pour {self.hours_worked} heure(s) de travail."
    
    def get_contract_type(self) -> str:
        return f"Type de contrat: Temps partiel."
    
class Freelance(Employee):
    def __init__(self, name: str, project_fee: int):
        self.name = name
        self.project_fee = project_fee

    def get_salary(self) -> str:
        return f"Le salaire de {self.name} est de : {self.project_fee} USD /projet."
    
    def get_contract_type(self) -> str:
        return "Type de contrat: Freelance."
    

def show_employee(employee: Employee) -> None:
    print(employee.introduce())
    print(employee.get_salary())
    print(employee.get_contract_type())


if __name__ == "__main__":

    workers = [
        FullTime("Steve", 100000),
        PartTime("Obed", 500, 200),
        Freelance("Stéphane", 2000000),
        FullTime("Gnak", 10000)
    ]

    for w in workers:
        show_employee(w)