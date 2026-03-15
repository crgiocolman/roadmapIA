import requests
import os
import json
from dotenv import load_dotenv
from zoho_auth import renovar_access_token

load_dotenv()

def obtener_campos(modulo, token):
    url = f"https://www.zohoapis.com/crm/v2/settings/fields?module={modulo}"

    headers = {
        "Authorization": f"Zoho-oauthtoken {token}"
    }

    respuesta = requests.get(url, headers=headers)
    datos = respuesta.json()
    #print(f"Datos obtenidos para {modulo}: {json.dumps(datos, indent=2)}")

    campos = []
    for campo in datos["fields"]:
        try:
            campos.append({
                "api_name": campo["api_name"],
                "tipo": campo["data_type"],
                "requerido": campo["system_mandatory"],
                "personalizado": campo["api_name"].endswith("__c")
            })
        except KeyError:
            print(f"Error: {KeyError.__traceback__}")
    return campos

def exportar_esqueleto(modulos):
    token = renovar_access_token()
    esqueleto = {}

    for modulo in modulos:
        print(f"Consultando {modulo}...")
        #Al poner [modulo] seguido de la variable esqueleto (de tipo objeto) se crea una nueva clave con el nombre del módulo y se le asigna el valor que devuelve la función
        esqueleto[modulo] = obtener_campos(modulo, token)

    with open("esqueleto_crm.json", "w") as f:
        json.dump(esqueleto, f, indent=2)

    print("Exportado a esqueleto_crm.json")

if __name__ == "__main__":
    exportar_esqueleto(["Leads", "Contacts", "Deals"])