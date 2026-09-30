import re

a = re.search(r' \+ ', 'Pierre Dupont + Paul Martin')
print(a.group())