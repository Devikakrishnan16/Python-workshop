import asyncio
from config import *
from telethon import TelegramClient ,events
import requests
from bs4 import BeautifulSoup

def scrape(url):
    file_name = "books.txt"
    req = requests.get(url)
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
           with open(file_name, 'a') as file:
                file.write(a + ":" + str(price) + '\n')
            
    return file_name


async def main():
    #main function
    bot = await TelegramClient('session', API_ID, API_HASH).start(
        bot_token= BOT_TOKEN
    )
    async with bot :
        print( "Logged in")
        @bot.on(events.NewMessage())#decorators
        async def handle_message(event):
            link = event.message.message
            file = scrape(link)
            user_id = event.sender.id
            await bot.send_file(user_id, file)
        await bot.run_until_disconnected()


asyncio.run(main())        