import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL du produit
url = "https://www.laredoute.fr/ppdp/prod-554346844.aspx"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify())
print(soup.title.text)
print(soup.find(class_='pdp-description-title'))
print(soup.h1)

# Extraire les informations du produit
catalog = soup.title.text.split(" | ")[0] if soup.title else ""
nom_commercial = soup.find("h2", class_="pdp-title title-sm-default").text.strip() if soup.find("h2", class_="pdp-title title-sm-default") else ""
marque = soup.find("span", class_="brand-name").text.strip() if soup.find("span", class_="brand-name") else ""
type_produit = "Meuble"
piece = "Salon"
categorie = "Assise"
sous_categorie = "Bout de canapé"
couleurs = "Noir"
matieres = "Métal"
profondeur = soup.find("span", class_="product-dimension-depth").text.strip() if soup.find("span", class_="product-dimension-depth") else ""
longueur = soup.find("span", class_="product-dimension-length").text.strip() if soup.find("span", class_="product-dimension-length") else ""
hauteur = soup.find("span", class_="product-dimension-height").text.strip() if soup.find("span", class_="product-dimension-height") else ""
prix = soup.find("span", class_="price").text.strip() if soup.find("span", class_="price") else ""
reference = soup.find("span", class_="product-reference").text.strip() if soup.find("span", class_="product-reference") else ""
photo = soup.find("img", class_="product-image")['src'] if soup.find("img", class_="product-image") else ""

# Créer une ligne pour le tableau
data = {
    "Catalogue": catalog,
    "Nom commercial": nom_commercial,
    "Marque": "marque",
    "Sous Marque": "",
    "Type de produit": type_produit,
    "Pièce": piece,
    "Catégorie": categorie,
    "Sous-catégorie": sous_categorie,
    "Couleurs": couleurs,
    "Matières": matieres,
    "Profondeur": profondeur,
    "Longueur": longueur,
    "Hauteur": hauteur,
    "Prix": prix,
    "Référence": reference,
    "URL": url,
    "Lien Web": url,
    "Photos Produits": photo,
}

# Ajouter la ligne dans un DataFrame pandas
df = pd.DataFrame([data])

# Afficher le tableau
print(df)

# Sauvegarder en fichier CSV
df.to_csv("produits.csv", index=False)
