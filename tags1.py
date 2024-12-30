import requests
from bs4 import BeautifulSoup

with open("main.html", "r") as f:
   main_docs = f.read()

soup = BeautifulSoup(main_docs, 'html.parser' )
print(soup.prettify())
print(soup.text)
print(soup.find(class_ = "muhammad"))
for link in soup.find_all("a"):
    print(link.get("href"))
    print(link.get("text"))

s = soup.find(id = "the best")
print(s) 

s1 = soup.span.get('a')
print(s1)

print(soup.span.get("class"))
print(soup.select("div"))

print(soup.find("div")[1])