import asyncio
from config import *
from telethon import TelegramClient ,events

async def main():
    #main function
    bot = await TelegramClient('session', API_ID, API_HASH).start(
        bot_token= BOT_TOKEN
    )
    async with bot :
        print( "Logged in")

asyncio.run(main())        