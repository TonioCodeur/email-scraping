from tinydb import Query, TinyDB, where

db = TinyDB("data.json", indent=4)
"""
db.insert({"name": "John Doe", "score": 42})
db.insert_multiple([
  {"name": "Jane Doe", "score": 42},
  {"name": "Bob Marley", "score": 43},
  {"name": "Curt Cobayn", "score": 44},
  {"name": "Jimmy Hendrix", "score": 45},
])
"""
User = Query()
bob = db.search(User.name.matches("Bob Marley"))
high_scores = db.search(where("score") > 40)
db.update({"score": 40}, where("name") == "John Doe")
db.update({"role": "user"})
print(bob)
print(high_scores)