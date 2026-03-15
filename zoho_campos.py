import requests
import asyncio
import os
import json
from dotenv import load_dotenv
from zoho_auth import renovar_access_token

load_dotenv()

async def obtener_campos(modulo, token):
    url = f"https://www.zohoapis.com/crm/v2/settings/fields?module={modulo}"

    headers = {
        "Authorization": f"Zoho-oauthtoken {token}"
    }

    respuesta = requests.get(url, headers=headers)
    datos = respuesta.json()

    campos = []
    for campo in datos["fields"]:
        try:
            campos.append({
                "api_name": campo["api_name"],
                "tipo": campo["data_type"],
                "requerido": campo["system_mandatory"],
                "personalizado": campo["api_name"].endswith("__c")
            })
        except KeyError as e:
            print(f"Campo faltante: {e}")
    return campos

async def exportar_esqueleto(modulos):
    token = renovar_access_token()

    resultados = await asyncio.gather(
        *[obtener_campos(modulo, token) for modulo in modulos]
    )

    esqueleto = {}
    for modulo, campos in zip(modulos, resultados):
        print(f"Consultando {modulo}...")
        #Al poner [modulo] seguido de la variable esqueleto (de tipo objeto) se crea una nueva clave con el nombre del módulo y se le asigna el valor que devuelve la función
        esqueleto[modulo] = campos

    with open("esqueleto_crm.json", "w") as f:
        json.dump(esqueleto, f, indent=2)

    print("Exportado a esqueleto_crm.json")

if __name__ == "__main__":
    asyncio.run(exportar_esqueleto(["Leads", "Contacts", "Deals"]))