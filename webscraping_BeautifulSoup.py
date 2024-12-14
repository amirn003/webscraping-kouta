import requests
from bs4 import BeautifulSoup

url = "https://www.laredoute.fr/ppdp/prod-554346844.aspx"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/'
}

response = requests.get(url, headers= headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    nom_commercial = soup.find('h1', class_='product-name').text.strip()
    prix = soup.find('span', class_='price').text.strip()

    data = {
        "Nom commercial": nom_commercial,
        "Prix": prix,
    }

    print(data)
else:
    print(f"Erreur lors du chargement de la page : {response.status_code}")
