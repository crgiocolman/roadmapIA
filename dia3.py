class Contacto:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def saludar(self):
        return f"Hola {self.nombre}"
    
c = Contacto("Sergio", "sergio@email.com")
print(c.saludar())
print(c.nombre)
print(c.email)

class ContactoZoho(Contacto):
    def __init__(self, nombre, email, id_zoho):
        super().__init__(nombre, email)
        self.id_zoho = id_zoho

    def info(self):
        return f"{self.nombre} | {self.email} | ID Zoho: {self.id_zoho}"
    
cz = ContactoZoho("Sergio", "sergio@email.com", "ZCR-00123")
print(cz.saludar())
print(cz.info())
print(cz.id_zoho)