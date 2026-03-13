import requests
import os
from dotenv import load_dotenv

load_dotenv()

def obtener_tokens():
    url = "https://accounts.zoho.com/oauth/v2/token"

    paramas = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("ZOHO_CLIENT_ID"),
        "client_secret": os.getenv("ZOHO_CLIENT_SECRET"),
        "redirect_uri": os.getenv("ZOHO_REDIRECT_URI"),
        "code": os.getenv("ZOHO_GRANT_TOKEN")
    }

    respuesta = requests.post(url, params=paramas)
    datos = respuesta.json()
    print(datos)
    return datos

if __name__ == "__main__":
    obtener_tokens()

def renovar_access_token():
    url = "https://accounts.zoho.com/oauth/v2/token"

    params = {
        "grant_type": "refresh_token",
        "client_id": os.getenv("ZOHO_CLIENT_ID"),
        "client_secret": os.getenv("ZOHO_CLIENT_SECRET"),
        "refresh_token": os.getenv("ZOHO_REFRESH_TOKEN")
    }

    respuesta = requests.post(url, params=params)
    datos = respuesta.json()
    return datos["access_token"]

token = renovar_access_token()
print(token)