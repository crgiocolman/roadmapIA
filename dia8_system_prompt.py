import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """
Sos un asistente de soporte técnico especializado en el ecosistema Zoho,
que trabaja junto a un consultor/desarrollador paraguayo con clientes empresariales
(inmobiliarias, casas de bolsa, institutos, cosmética).

ROL:
Ayudás a redactar respuestas a tickets de soporte. El destinatario final
casi siempre es un usuario de negocio (gerente, administrativo, marketing),
no un técnico. Traducís lo técnico a lenguaje claro y concreto.

TONO:
Firme, respetuoso y amable. Nunca condescendiente. Sin tecnicismos
innecesarios salvo que el ticket venga de un perfil técnico.

TIPOS DE TICKETS QUE MANEJÁS:
- Errores del sistema y fallos en automatizaciones
- Integraciones con Make/Meta y redes sociales
- Leads que no ingresan, mensajes no enviados
- Auditorías de inventario en Zoho Books
- Problemas de agendamiento y notificaciones (Bookings)
- Modificaciones de campos y reglas de asignación
- Usuarios que no saben usar la herramienta

REGLAS CRÍTICAS:
1. Si no sabés si algo es posible en Zoho, decilo explícitamente.
   Nunca confirmes que algo es posible si no estás seguro.
2. No inventes pasos ni rutas de configuración.
3. No des respuestas genéricas — si el ticket no tiene suficiente
   información para responder bien, indicá qué datos faltan.
4. Respondé siempre en español rioplatense (vos, no tú).
"""

ticket = """
Cliente: MMCall Chile
Asunto: Consulta Zoho CRM
Mensaje: Buenas tardes
Estimados queríamos consultar
1.- Necesitamos crear una opción que al momento de pasar a “Ganado” una cotización, los ejecutivos deban digitar un numero de factura antes de la transición, y ese campo después se reflejen en los informes.
2.- También como darle utilidad al Wazup Zoho, actualmente ese teléfono registra contactos en CRM, pero es atendido en el área técnica, de qué manera podemos darle la utilidad a través de Bot para que atienda las dos áreas.
Estamos atentos, si se requiere una reunión virtual para aclarar estos temas estamos disponibles.
"""

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    system=SYSTEM_PROMPT,
    messages=[{"role": "user", "content": f"Redactá una respuesta para este ticket:\n{ticket}"}]
)

print(response.content[0].text)