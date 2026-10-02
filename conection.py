import requests
from config import Token

url = f"https://api.telegram.org/bot{Token}/getMe"

response = requests.get(url, timeout=10)

print(response.status_code)
print(response.text)