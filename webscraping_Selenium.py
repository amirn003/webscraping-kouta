from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Configuration de Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Exécution en arrière-plan
service = Service('/Users/amir/webdrivers/chromedriver-mac-x64/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL du produit
url = "https://www.laredoute.fr/ppdp/prod-554346844.aspx"

# Charger la page
driver.get(url)

# Attendre que le contenu soit chargé
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pdp-title")))

# Faire défiler la page pour charger tout le contenu
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # Attendre le chargement du contenu

# Obtenir le contenu de la page
html_content = driver.page_source

# Utiliser BeautifulSoup pour parser le contenu
soup = BeautifulSoup(html_content, 'html.parser')

# Extraire les informations du produit
catalog = soup.title.text.split(" | ")[0] if soup.title else ""
nom_commercial = soup.find("h1", class_="pdp-title").text.strip() if soup.find("h1", class_="pdp-title") else ""
marque = soup.find("span", class_="brand-name").text.strip() if soup.find("span", class_="brand-name") else ""
type_produit = "Meuble"
piece = "Salon"
categorie = "Assise"
sous_categorie = "Bout de canapé"
couleurs = soup.find("span", class_="color-name").text.strip() if soup.find("span", class_="color-name") else ""
matieres = "Métal"

# Extraire les dimensions
dimensions = soup.find("div", class_="product-dimensions")
profondeur = ""
longueur = ""
hauteur = ""
if dimensions:
    for dim in dimensions.find_all("li"):
        if "Profondeur" in dim.text:
            profondeur = dim.text.split(":")[1].strip()
        elif "Longueur" in dim.text:
            longueur = dim.text.split(":")[1].strip()
        elif "Hauteur" in dim.text:
            hauteur = dim.text.split(":")[1].strip()

prix = soup.find("span", class_="price-sales").text.strip() if soup.find("span", class_="price-sales") else ""
reference = soup.find("span", class_="product-reference").text.strip() if soup.find("span", class_="product-reference") else ""
photo = soup.find("img", class_="pdp-image")['src'] if soup.find("img", class_="pdp-image") else ""

# Créer une ligne pour le tableau
data = {
    "Catalogue": catalog,
    "Nom commercial": nom_commercial,
    "Marque": marque,
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

# Fermer le navigateur
driver.quit()
