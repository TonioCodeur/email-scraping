# Python Sandbox — self-taught learning journey

**[English](#english) · [Français](#français)**

---

## English

This repository gathers everything I have learned in Python on my own: exercises, small scripts, step-by-step tutorials and mini-projects. It is not a single application. It is more of a **learning logbook**, started in September 2024 and expanded as I keep studying.

### Why this project

- **Learning by doing.** Each concept (lists, classes, generators, regular expressions…) gets its own script so I can work with it hands-on.
- **Keeping a record.** The repository serves as my memory. When I am unsure about a syntax or a concept, I come back to the matching exercise.
- **Progressing step by step.** From the basics (variables, loops, files) to object-oriented programming and advanced features, then to more complete projects (game, database, encryption, scraping).
- **Learning Git along the way.** The commit history also reflects my learning of version control.

### Contents

| Folder / files | What I practiced |
|---|---|
| Root scripts | The basics: Fibonacci, BMI calculator, "higher or lower" games, reading/writing text and JSON files, the `os` module, file sorting, type hints, `datetime`… |
| `POO/` | Object-oriented programming: classes, instance initialization, `dataclass`, inheritance, polymorphism, `classmethod` / `staticmethod`, `__str__` |
| `Python_avancé/` | One folder per concept: list comprehensions, `map` / `filter`, `lambda`, `enumerate`, `zip`, iterators, generators, `*args` / `**kwargs`, sets, ternary operators, docstrings, regular expressions, mutability |
| `db/` | Data persistence: SQLite, JSON, TinyDB |
| `todo-list/` | An object-oriented to-do list, with the logic kept separate from the constants |
| `Tuto-Game/` | A mini-game built with **pygame** (player, projectiles, monsters, animations) |
| `FilesEncrypt/`, `chiffrement.py`, `encrypt.py` | File encryption with **cryptography** (Fernet) and a Tkinter interface |
| `Scrapping/`, `email-scraping.py` | Web scraping with **requests** and **BeautifulSoup**, email extraction |
| `Faker/`, `typer/` | Exploring libraries: fake data generation, building command-line tools |

Folder names, comments and messages in the code are in French.

### Running the scripts

Each script is standalone and can be run directly:

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
python path/to/the_script.py
```

`requirements.txt` only covers encryption. For the other folders, install the libraries as needed: `pygame`, `requests`, `beautifulsoup4`, `faker`, `tinydb`, `typer`.

> Run the game from the repository root (`python Tuto-Game/main.py`), because the image paths are relative to the root.

### What's next

This repository keeps growing as I learn. My next goals are unit testing (the `Tests unitaires/` folder is ready for it) and more complete projects that combine several of these concepts.

---

## Français

Ce dépôt rassemble tout ce que j'ai appris en Python par moi-même : exercices, petits scripts, tutoriels suivis pas à pas et mini-projets. Ce n'est pas une application unique. C'est plutôt un **carnet de bord** de ma progression, commencé en septembre 2024 et complété au fil de mes études.

### Pourquoi ce projet

- **Apprendre en pratiquant.** Chaque notion (listes, classes, générateurs, expressions régulières…) a son propre script pour la manipuler concrètement.
- **Garder une trace.** Le dépôt me sert de mémoire. Quand j'ai un doute sur une syntaxe ou un concept, je reviens voir l'exercice correspondant.
- **Progresser pas à pas.** On part des bases (variables, boucles, fichiers) pour aller vers la programmation orientée objet, les notions avancées, puis des projets plus complets (jeu, base de données, chiffrement, scraping).
- **Apprendre Git en même temps.** L'historique des commits montre aussi mon apprentissage du versionnement.

### Contenu

| Dossier / fichiers | Ce que j'y ai travaillé |
|---|---|
| Scripts à la racine | Les bases : Fibonacci, calcul d'IMC, jeux « plus ou moins », lecture/écriture de fichiers texte et JSON, module `os`, tri de fichiers, annotations de types, `datetime`… |
| `POO/` | Programmation orientée objet : classes, initialisation d'instances, `dataclass`, héritage, polymorphisme, `classmethod` / `staticmethod`, `__str__` |
| `Python_avancé/` | Un dossier par notion : compréhensions de listes, `map` / `filter`, `lambda`, `enumerate`, `zip`, itérateurs, générateurs, `*args` / `**kwargs`, sets, opérateurs ternaires, docstrings, expressions régulières, mutabilité |
| `db/` | Persistance des données : SQLite, JSON, TinyDB |
| `todo-list/` | Une todo-list orientée objet, avec la logique séparée des constantes |
| `Tuto-Game/` | Un mini-jeu avec **pygame** (joueur, projectiles, monstres, animations) |
| `FilesEncrypt/`, `chiffrement.py`, `encrypt.py` | Chiffrement de fichiers avec **cryptography** (Fernet) et une interface Tkinter |
| `Scrapping/`, `email-scraping.py` | Web scraping avec **requests** et **BeautifulSoup**, extraction d'e-mails |
| `Faker/`, `typer/` | Découverte de bibliothèques : génération de fausses données, création d'outils en ligne de commande |

### Lancer les scripts

Chaque script est indépendant et se lance directement :

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
python chemin/vers/le_script.py
```

`requirements.txt` ne couvre que le chiffrement. Pour les autres dossiers, il faut installer les bibliothèques au besoin : `pygame`, `requests`, `beautifulsoup4`, `faker`, `tinydb`, `typer`.

> Le jeu se lance depuis la racine du dépôt (`python Tuto-Game/main.py`), car les chemins vers les images sont relatifs à la racine.

### La suite

Ce dépôt continue de grandir au rythme de mon apprentissage. Les prochaines étapes que je vise sont les tests unitaires (le dossier `Tests unitaires/` est prêt à les accueillir) et des projets plus aboutis qui combinent plusieurs de ces notions.
