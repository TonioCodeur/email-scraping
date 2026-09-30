import re

text = "item01 | item02 - item03 | item04 | item05"

a = re.split(r"\| | - ", text)
print(a)