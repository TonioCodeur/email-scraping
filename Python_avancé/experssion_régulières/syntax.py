import re

print("\tBonjour")
print(r"\tBonjour")

a = re.match(r".+", "Pierre Dupont")
print(a)
print(a.group())

b = re.match(r"(\w+)\s(\w+)", "Pierre Dupont")
print(b.group(0))
print(b.group(1))
print(b.group(2))

c = re.match(r"(?P<prenom>\w+) (?P<nom>\w+)", "Pierre Dupont")
print(c.group("prenom"))
print(c.group("nom"))
print(c.groups())
print(c.groupdict())