from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
zoho_url = os.getenv("ZOHO_URL")

print(api_key)
print(zoho_url)