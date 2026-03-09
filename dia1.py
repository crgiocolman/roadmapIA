nombre = "Sergio"
edad = 25
activo = True
nada = None

print(f"Hola {nombre}, tienes {edad} años")
print(f"Activo? {activo}")
print(f"Que es None? {nada}")
print(type(nombre))
print(type(edad))
print(type(nada))

# Listas (arrays en JS)
lenguajes = ["JavaScript", "PHP", "Python"]
print(lenguajes[0])
print(len(lenguajes))
lenguajes.append("Deluge")
print(lenguajes)

# Diccionarios (objetos en JS)
perfil = { 
    "nombre": "Sergio", 
    "edad": 25, 
    "activo": True 
}
print(perfil["nombre"])
print(perfil.get("email", "No tiene email"))