# Sandbox Python — mon apprentissage en autodidacte

Ce dépôt rassemble tout ce que j'ai appris en Python par moi-même : exercices, petits scripts, tutoriels suivis pas à pas et mini-projets. Ce n'est pas une application unique. C'est plutôt un **carnet de bord** de ma progression, commencé en septembre 2024 et complété au fil de mes études.

## Pourquoi ce projet

- **Apprendre en pratiquant.** Chaque notion (listes, classes, générateurs, expressions régulières…) a son propre script pour la manipuler concrètement.
- **Garder une trace.** Le dépôt me sert de mémoire. Quand j'ai un doute sur une syntaxe ou un concept, je reviens voir l'exercice correspondant.
- **Progresser pas à pas.** On part des bases (variables, boucles, fichiers) pour aller vers la programmation orientée objet, les notions avancées, puis des projets plus complets (jeu, base de données, chiffrement, scraping).
- **Apprendre Git en même temps.** L'historique des commits montre aussi mon apprentissage du versionnement.

## Contenu

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

## Lancer les scripts

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

## La suite

Ce dépôt continue de grandir au rythme de mon apprentissage. Les prochaines étapes que je vise sont les tests unitaires (le dossier `Tests unitaires/` est prêt à les accueillir) et des projets plus aboutis qui combinent plusieurs de ces notions.
