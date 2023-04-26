import requests
from bs4 import BeautifulSoup
URL = "https://books.toscrape.com/"

req = requests.get(URL)
source_code = req.content

soup = BeautifulSoup(source_code , 'lxml')

articles = soup.find_all('article')
for article in articles:
    h3 = article.find('h3')
    a = h3.find('a')
    print(a.text)

for j in articles:
    div = j.find('div', class_="product_price")
    p= div.find('p')
    print(p.text)




