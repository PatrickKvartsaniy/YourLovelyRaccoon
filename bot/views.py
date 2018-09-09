import json
import aiohttp

from .bot import Conversation

class Raccoon(Conversation):
    MESSAGE_TEMPLATE = "{} {}. \n Деталі на нашій сторінці - {}"

    def __init__(self, token, db, loop):
        super().__init__(token, db, loop)

    async def _handler (self, message):
        if message['text'] == "/events":
            events = await self.getData("FutureEvents")
            message_head = "Зараз в нас плануються такі івенти:"
            await self.sendMessage(message['chat']['id'], message_head)
            for event in events:
                await self.sendMessage(message['chat']['id'],
                                       self.MESSAGE_TEMPLATE.format(event['title'],
                                                                    event['date'],
                                                                    event['link']))
        elif message['text'] == "/news":
            news = await self.getData("LastPosts")
            message_head = "Останні новини:"
            await self.sendMessage(message['chat']['id'], message_head)
            for post in news:
                await self.sendMessage(message['chat']['id'],
                                       self.MESSAGE_TEMPLATE.format(post['title'],
                                                                    post['date'],
                                                                    post['link']))
        elif message['text'] == "/subscribe":
            try:
                sub = message['from']
                result = await self.save_sub(sub['id'], sub['first_name'], sub['username'])
                if result == "Exist":
                    await self.sendMessage(message['chat']['id'], f"Тю {message['from']['first_name']}, ти ж вже з нами")
                elif result == "Done":
                    await self.sendMessage(message['chat']['id'], f"{message['from']['first_name']}, вітаю в падпісотє")
            except Exception as e:
                print(e)
