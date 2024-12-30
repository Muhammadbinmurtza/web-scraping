import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def getting_data(url, path):
    r = requests.get(url)
    with open(path , "w") as f:
        f.write(r.text)
url = "https://texasroadhousemenu.me/"

getting_data(url, "texasroadhouse.html")

