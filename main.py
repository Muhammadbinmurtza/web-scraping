import requests
from bs4 import BeautifulSoup

def fetchFromWeb(url, path):
    r = requests.get(url)
    with open(path, 'w') as f:
        data = f.write(r.text)
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

fetchFromWeb(url, "data/index.html")
with open("data/index.html" , "r") as f:
    data = f.read()

soup = BeautifulSoup(data , "html.parser")

# print(soup.find_all("div"))
# for heading in soup.find_all("div"):
#     print(heading.get_text())

# for link in soup:
#     print(soup.get("href"))
# print(soup.prettify())
# print("\n\n\n\n  how this happened \n\n\n\n\n")
# for the_text in soup.find(class_ = "icon-ok"):
#     print(the_text.get_text())
all_classes = set()
for classe  in soup.find_all(class_ = True):
    classes = classe.get("class")
    all_classes.update(classes)

print(all_classes)


elements = soup.find_all(class_ = "breadcrumb")
for element in elements:
    print(element.get_text(strip=True))

print("\n\n\n\n\n\n\n\   hey \n\n\n\n\n")

print(soup.title.string)