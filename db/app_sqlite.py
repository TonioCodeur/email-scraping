import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""
           CREATE TABLE IF NOT EXISTS employees (
             firstname text,
             lastname text,
             age int
           )
           """)
employees = {"firstname": "Jane", "lastname": "Doe", "age": 28}
c.execute("INSERT INTO employees VALUES (:firstname, :lastname, :age)", employees)
conn.commit()
conn.close()