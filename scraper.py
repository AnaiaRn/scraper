import requests
from bs4 import BeautifulSoup
import pandas as pd

# 🔗 URL du site à scraper
url = "https://torolalana.gov.mg/fr/services/regions-et-districts/"

# 🔧 En-têtes pour éviter les blocages
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Vérifie les erreurs HTTP

    soup = BeautifulSoup(response.text, "html.parser")

    # 🧠 Extraire le texte de balises courantes
    elements = {
        "h1": [el.get_text(strip=True) for el in soup.find_all("h1")],
        "h2": [el.get_text(strip=True) for el in soup.find_all("h2")],
        "h3": [el.get_text(strip=True) for el in soup.find_all("h3")],
        "h4": [el.get_text(strip=True) for el in soup.find_all("h4")],
        "p": [el.get_text(strip=True) for el in soup.find_all("p")],
    }

    # 🧹 Supprimer les éléments vides
    for tag in elements:
        elements[tag] = [txt for txt in elements[tag] if txt]

    # 🔎 Vérification du contenu
    total = sum(len(v) for v in elements.values())
    if total == 0:
        print("⚠️ Aucune donnée trouvée. Vérifie la structure HTML du site.")
    else:
        print("✅ Contenu extrait :\n")
        for tag, texts in elements.items():
            if texts:
                print(f"\n--- {tag.upper()} ---")
                for t in texts:
                    print(f"- {t}")

        # 💾 Sauvegarde dans un CSV
        data = []
        for tag, texts in elements.items():
            for t in texts:
                data.append({"Balise": tag, "Texte": t})

        df = pd.DataFrame(data)
        df.to_csv("resultats.csv", index=False, encoding="utf-8-sig")

        print("\n✅ Données enregistrées dans resultats.csv")

except requests.exceptions.RequestException as e:
    print("❌ Erreur lors de la requête :", e)
