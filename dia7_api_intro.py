import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

messages = [
    {"role": "user", "content": "¿Cómo creo un campo personalizado en Zoho CRM?"},
]

response1 = client.messages.create(
    model="claude-opus-4-5",
    system="Sos un asistente especializado en soporte técnico de Zoho CRM. Respondés siempre en español, de forma concisa y técnica.",
    max_tokens=1024,
    messages = messages
)

print("Respuesta 1:", response1.content[0].text)
print("Tokens:", response1.usage.input_tokens, "/", response1.usage.output_tokens)

messages.append({"role": "assistant", "content": response1.content[0].text})
messages.append({"role": "user", "content": "¿Y cómo lo hago obligatorio?"})

print("f{messages=}", messages)

response2 = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    system="Sos un asistente especializado en soporte técnico de Zoho CRM. Respondés siempre en español, de forma concisa y técnica.",
    messages=messages
)

print("\nRespuesta 2:", response2.content[0].text)
print("Tokens:", response2.usage.input_tokens, "/", response2.usage.output_tokens)