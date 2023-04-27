import requests
from bs4 import BeautifulSoup
URL = "http://books.toscrape.com/"

def scrape(URL):
    req = requests.get(URL)
    source_code = req.content

    soup = BeautifulSoup(source_code , 'lxml')

    articles = soup.find_all('article')
    for article in articles:
        h3 = article.find('h3')
        a = (h3.find('a')).text
        price = article.find('div' , class_= "product_price")
        price= price.find('p')
        price = price.text[1:]
        print(type(price))
        price = float(price)
        print(type(price))
        print(price)
        if price <50:
           with open('book.txt', 'a') as file:
                file.write(a + ":" + str(price) + '\n')


scrape("http://books.toscrape.com/")



