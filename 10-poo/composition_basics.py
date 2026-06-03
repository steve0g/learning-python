"""
COMPOSITION BASICS - V1.0
--------------------------
This module demonstrates object composition in Python.
A class can contain another class as an attribute (HAS-A relationship),
as opposed to inheritance which represents an IS-A relationship.
"""

class Phone:
    def __init__(self, brand: str, number: str):
        self.brand = brand
        self.number = number

    def call(self, contact: str):
        return f"Appel vers {contact} depuis {self.number}"
    

class Employee:
    def __init__(self, name: str, phone_brand: str, phone_number: str):
        self.name = name
        self.phone = Phone(phone_brand, phone_number)

    def introduce(self):
        return f"Je suis {self.name}, mon numéro est {self.phone.number}"
    

employee_1 = Employee("Obed", "iPhone 17", "0102030405")
employee_2 = Employee("Elon", "iPhone 18", "0105040302")
print(employee_1.introduce())
print(employee_1.phone.call("Obed"))
print(employee_2.introduce())
print(employee_2.phone.call("Elon"))
