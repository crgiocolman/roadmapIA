import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(respuesta.status_code)
print(respuesta.json())

datos = respuesta.json()
print(datos["name"])
print(datos["email"])
print(datos["company"]["name"])