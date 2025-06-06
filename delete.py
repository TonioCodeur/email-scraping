import os

import psutil


def fermer_processus_utilisant_chemin(chemin):
    """
    Ferme tous les processus qui utilisent un chemin spécifique.
    
    Args:
        chemin (str): Le chemin à vérifier
    """
    chemin_normalise = os.path.normpath(chemin)
    print(f"Recherche des processus utilisant: {chemin_normalise}")
    
    processus_fermes = 0
    
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            # Vérifier si le processus a des fichiers ouverts
            if proc.info['open_files']:
                for fichier in proc.info['open_files']:
                    if chemin_normalise in os.path.normpath(fichier.path):
                        print(f"Processus {proc.info['pid']} ({proc.info['name']}) utilise {fichier.path}")
                        try:
                            proc.terminate()
                            print(f"Processus {proc.info['pid']} terminé avec succès")
                            processus_fermes += 1
                        except Exception as e:
                            print(f"Impossible de terminer le processus {proc.info['pid']}: {e}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    print(f"{processus_fermes} processus ont été fermés")

# Exécuter la fonction pour fermer les processus utilisant le chemin spécifié
if __name__ == "__main__":
    chemin_cible = r"c:/users/postgres"
    fermer_processus_utilisant_chemin(chemin_cible)
