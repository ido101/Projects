import requests
from bs4 import BeautifulSoup

res = requests.get("https://8200university.co.il/ctf-challenge-4-7352/")
soup = BeautifulSoup(res.text, "html.parser")
print(soup.prettify())