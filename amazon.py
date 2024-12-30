import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
# print(ua.chrome)

header = {'User-Agent':str(ua.chrome)}

url = "https://www.amazon.in/s?k=iphone+14&crid=275M7VXV6O6EI&sprefix=iphone+1%2Caps%2C600&ref=nb_sb_noss_2"

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(url,  headers=header)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())