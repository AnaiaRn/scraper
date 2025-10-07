import os
from PyPDF2 import PdfReader

# Dossiers
input_dir = "pdf_inputs"
output_dir = "pdf_outputs"

# Crée le dossier de sortie s'il n'existe pas
os.makedirs(output_dir, exist_ok=True)

# Parcours de tous les fichiers PDF dans le dossier d'entrée
for fichier in os.listdir(input_dir):
    if fichier.endswith(".pdf"):
        chemin_pdf = os.path.join(input_dir, fichier)
        nom_sans_ext = os.path.splitext(fichier)[0]
        sortie_txt = os.path.join(output_dir, f"texte_extrait_{nom_sans_ext}.txt")

        print(f"📄 Traitement de : {fichier} ...")

        # Lecture du PDF
        reader = PdfReader(chemin_pdf)
        texte_total = ""
        for i, page in enumerate(reader.pages):
            texte_total += f"\n--- Page {i+1} ---\n"
            texte_total += page.extract_text() or ""

        # Sauvegarde du texte extrait
        with open(sortie_txt, "w", encoding="utf-8") as f:
            f.write(texte_total)

        print(f"✅ Texte enregistré dans : {sortie_txt}\n")

print("🚀 Traitement terminé pour tous les PDFs.")

