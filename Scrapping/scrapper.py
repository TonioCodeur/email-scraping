import requests
from bs4 import BeautifulSoup

url = "https://www.docstring.fr/api/books_to_scrape/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

with open("index.html", "w") as f:
    f.write(soup.prettify())