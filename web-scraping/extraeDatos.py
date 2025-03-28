import requests
from bs4 import BeautifulSoup, Comment
import re

# URL del servidor local
url = "http://127.0.0.1:8000/victima.html"

# Obtener la respuesta del servidor
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extraer enlaces
links = [a["href"] for a in soup.find_all("a", href=True)]
print("Enlaces encontrados:")
print(links)

# Extraer comentarios en el HTML
comments = [comment for comment in soup.find_all(string=lambda text: isinstance(text, Comment))]
print("\nComentarios encontrados:")
print(comments)

# Extraer direcciones de correo electrónico
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
print("\nCorreos electrónicos encontrados:")
print(emails)
