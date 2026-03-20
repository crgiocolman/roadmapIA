import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def llamar_claude(mensaje, max_tokens=1024):
    try:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": mensaje}]
        )
        return response.content[0].text

    except anthropic.AuthenticationError:
        print("❌ API key inválida o expirada")
        return None

    except anthropic.RateLimitError:
        print("⏳ Límite de requests alcanzado, esperá un momento")
        return None

    except anthropic.APIStatusError as e:
        print(f"❌ Error de API: {e.status_code} — {e.message}")
        return None

    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None
    
# Prueba normal
resultado = llamar_claude("Decime una ventaja de Zoho CRM en una oración.")
print(resultado)

# Prueba con API key inválida
client_malo = anthropic.Anthropic(api_key="sk-ant-falsa-123")
try:
    client_malo.messages.create(
        model="claude-opus-4-5",
        max_tokens=10,
        messages=[{"role": "user", "content": "hola"}]
    )
except anthropic.AuthenticationError:
    print("✅ AuthenticationError capturado correctamente")

# Prueba con max_tokens inválido
try:
    client.messages.create(
        model="claude-opus-4-5",
        max_tokens=-1,
        messages=[{"role": "user", "content": "hola"}]
    )
except anthropic.BadRequestError as e:
    print(f"✅ BadRequestError capturado: {e.status_code}")