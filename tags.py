import requests
from bs4 import BeautifulSoup


with open('sample.html', 'r') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title.string)
print(soup.div)
print(soup.find_all("div"))
print(soup.find_all("div")[1])

for link in soup.find_all("a"):
    print(link.get("href"))
    print(link.get_text())
s = soup.find(id="link3")
print(s)
print(s.get('href'))
print(soup.select("div.italic"))
print(soup.select("span#italic"))
print(soup.span.get("class"))
print(soup.find(id = "italic"))
print(soup.find(class_ = "italic")) 
print(soup.find_all(class_= "italic"))
for child in soup.find(class_ = "container").children:
    print(child)

i = 1
for parent in soup.find(class_  = "box").parents:
    i += 1
    print(parent)
    if i == 2 :
        break

cant = soup.find(class_ = "container")
cant.name = "span"
print(cant)
cant['class'] = "the"
cant.string = "who the fuck are you"
print(cant)

ultag = soup.new_tag("thebest")
ultag.string = "home"
litag = soup.new_tag("mian100")
litag.string = "about"
ultag.append(litag)

soup.html.body.insert(0, ultag)
with open("recreation.html" , "w") as f:
    f.write(str(soup))
for i in soup.find_all("a"):
    print(i.get('href'))
with open("muhammad.html", "w") as f:
    f.write(str(soup))
cont = soup.find(class_= "container")
print(cont.has_attr("id"))
print(cont.has_attr("class"))
print(cont.has_attr("contenteditable"))

def has_class_but_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

results = soup.find_all(has_class_but_no_id)

def has_content(tag):
    return tag.has_attr("content") 
results = soup.find_all(has_content)
for result in results:
    print(result, "\n\n")