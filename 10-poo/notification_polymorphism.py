"""
NOTIFICATION POLYMORPHISM DEMO - V1.0
--------------------------------------
Ce script illustre le polymorphisme en Python à travers
un système de notifications multi-canal (Email, SMS, Push).
Une fonction externe notify() traite n'importe quel type
de notification grâce à l'héritage et l'override de méthodes.
"""

class Notification:
    def envoyer(self) -> str:
        return "Message envoyé"
    
class EmailNotification(Notification):
    def __init__(self, email: str, message: str):
        self.email = email
        self.message = message

    def envoyer(self) -> str:
        return f"Votre Email a été envoyé à {self.email} avec le message : {self.message}"

class SMSNotification(Notification):
    def __init__(self, numero: str, message: str):
        self.numero = numero
        self.message = message

    def envoyer(self) -> str:
        return f"Votre SMS a été envoyé avec succès au {self.numero} avec le message : {self.message}"
    
class PushNotification(Notification):
    def __init__(self, nom_appareil):
        self.nom_appareil = nom_appareil

    def envoyer(self) -> str:
        return f"Notification envoyé avec succès sur {self.nom_appareil}"
    
def notify(notification: Notification):
    print(notification.envoyer())


liste_notif = [
    EmailNotification("ko@gmail.com", "Votre commande est confirmée."),
    SMSNotification("+2250700000000", "Code OTP : 4821"),
    PushNotification("iPhone de Elon"),
    EmailNotification("gnak@gmail.com", "Nouveau client inscrit.")
]

for l in liste_notif:
    notify(l)