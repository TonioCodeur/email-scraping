from pathlib import Path

try:
    path = Path(__file__).parent / "fichiers"
    path.mkdir(parents=True, exist_ok=True)

    file_path = path / "readme.md"
    file_path.touch(exist_ok=True)
    print(file_path)
    file_path.write_text("Hello World", encoding="utf-8")
    print(file_path.read_text(encoding="utf-8"))
except PermissionError:
    print("Erreur de permission. Vérifiez vos droits d'accès.")
except OSError as e:
    print(f"Erreur système : {e}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")

for f in Path.home().iterdir():
  print(f)
for f in path.iterdir():
  print(f)