import requests
import os
from dotenv import load_dotenv
from zoho_auth import renovar_access_token

load_dotenv()

def obtener_modulos():
    token = renovar_access_token()

    url = "https://www.zohoapis.com/crm/v2/settings/modules"

    headers = {
        "Authorization": f"Zoho-oauthtoken {token}"
    }

    respuesta = requests.get(url, headers=headers)
    datos = respuesta.json()
    for modulo in datos["modules"]:
        print(f"{modulo['api_name']} | {modulo['module_name']}")


obtener_modulos()