import datetime
import subprocess

# Récupérer la date du jour
date_du_jour = datetime.datetime.now().strftime("%d/%m/%Y")

# Message du commit
commit_message = f"commit du {date_du_jour}"

# Exécuter les commandes Git
try:
    # Ajouter tous les fichiers
    subprocess.run(["git", "add", "."], check=True)

    # Faire le commit avec la date du jour
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Pousser le commit vers le dépôt distant
    subprocess.run(["git", "push"], check=True)

    print("✅ Commit et push réussis !")
except subprocess.CalledProcessError as e:
    print(f"❌ Une erreur s'est produite : {e}")
