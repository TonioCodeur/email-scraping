import shutil
from pathlib import Path

home_path = Path.home()
print(home_path)
path = Path(__file__).resolve()
current_path = path.parent # ou Path.cwd()
print(current_path)
# file_path = current_path / "pathlid"
# file_path = current_path.joinpath("pathLib")
# file_path.mkdir(parents=True, exist_ok=True)
file_path = current_path.joinpath("fichier.txt")
file_path.touch()
# if file_path.exists():
  # print("File exists")
  # file_path.unlink()
print(file_path)
file_path = file_path.parent
file_path = file_path / "pathlib"
file_path.mkdir(exist_ok=True)
print(file_path)
# file_path.rmdir()
extention = (current_path / "pathlib" / "fichier.py").suffix
print(file_path.suffix)
print(extention)
print(file_path.name)
print(file_path.stem)
print(file_path.suffix)
print(file_path.suffixes)
print(file_path.parts)
print(file_path.exists())
print(file_path.is_file())
print(file_path.is_dir())
print(file_path.parent)
print(file_path)
# file_path.rmdir()
shutil.rmtree(file_path)