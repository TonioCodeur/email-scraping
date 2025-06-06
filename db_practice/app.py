import sqlite3

from faker import Faker

# Création de 10 utilisateurs avec Faker
fake = Faker(locale="fr_FR")
users = []
for _ in range(10):
    user = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "age": fake.random_int(min=18, max=80)
    }
    users.append(user)

with sqlite3.connect("database_practice.db") as conn:
  c = conn.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS users (
    firstname text,
    lastname text,
    age int)""")

  # Insertion des utilisateurs dans la base de données
  for user in users:
      c.execute("INSERT INTO users VALUES (:firstname, :lastname, :age)", user)
      
  # Selection des utilisateurs dans la base de données
  c.execute("SELECT * FROM users")
  data = c.fetchall()
  for user in data:
      print(user)