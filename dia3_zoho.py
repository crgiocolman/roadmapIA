import json

class RegistroZoho:
    def __init__(self, datos):
        self.datos = datos

    def obtener(self, campo):
        try:
            return self.datos[campo]
        except KeyError:
            return f"Campo '{campo}' no existe"

    def a_json(self):
        return json.dumps(self.datos, indent=2)    

registro = RegistroZoho({
    "nombre": "Sergio",
    "email": "sergio@email.com",
    "empresa": "Freelance",
    "id_zoho": "ZCR-00123"
})

print(registro.obtener("nombre"))
print(registro.obtener("telefono"))
print(registro.a_json())

texto_json = '{"nombre": "Sergio", "email": "sergio@email.com"}'
datos = json.loads(texto_json)
print(datos["nombre"])