from pathlib import Path

sort_dir = Path.home() / "Downloads"
sort_dir.mkdir(exist_ok=True)
dir = {
  ".png": "images",
  ".jpg": "images",
  ".gif": "images",
  ".jpeg": "images",
  ".webp" : "images",
  ".ico": "images",
  ".svg": "images",
  ".mp3": "musiques",
  ".wav": "musiques",
  ".flac": "musiques",
  ".ogg": "musiques",
  ".m4a": "musiques",
  ".mkv": "vidéos",
  ".avi": "vidéos",
  ".mov": "vidéos",
  ".wmv": "vidéos",
  ".json": "json",
  ".mp4": "vidéos",
  ".zip": "archives",
  ".rar": "archives",
  ".7z": "archives",
  ".tar": "archives",
  ".gz": "archives",
  ".bz2": "archives",
  ".pdf": "documents",
  ".txt": "documents",
  ".iso": "disques vituels",
  ".exe": "logiciels",
  ".msi": "logiciels",
  ".bat": "logiciels",
  ".vbs": "logiciels",
}
files = [f for f in sort_dir.iterdir() if f.is_file()]
print(f"voici les dossiers dans lesquels sont rangé les fichiers : {sort_dir}")
for value in set(dir.values()):
  print(value)
for f in files:
    output_dir = sort_dir / dir.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    destination = output_dir / f.name
    if not destination.exists():
        f.rename(destination)
    else:
        print(f"Le fichier {f.name} existe déjà dans {output_dir}. Ignoré.")