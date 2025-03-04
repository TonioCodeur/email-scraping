from pathlib import Path

sort_dir = Path.home() / "Downloads"
sort_dir.mkdir(exist_ok=True)
dir = {
  ".png": "images",
  ".jpg": "images",
  ".gif": "images",
  ".jpeg": "images",
  ".webp" : "images",
  ".json": "json",
  ".mp4": "vidéos",
  ".zip": "archives",
  ".rar": "archives",
  ".pdf": "documents",
  ".txt": "documents",
  ".mp3": "ùusiquess",
  ".iso": "disques vituels",
  ".exe": "logiciels",
}
files = [f for f in sort_dir.iterdir() if f.is_file()]
print(f"voici les dossiers dans lesquels sont rangé les fichiers : {sort_dir}")
for value in dir.values():
  print(value)
for f in files:
    output_dir = sort_dir / dir.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    destination = output_dir / f.name
    if not destination.exists():
        f.rename(destination)
    else:
        print(f"Le fichier {f.name} existe déjà dans {output_dir}. Ignoré.")