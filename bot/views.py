import json
import aiohttp

from .bot import Conversation

class Raccoon(Conversation):
    MESSAGE_TEMPLATE = "{} {}. Деталі на нашій сторінці - {}"

    def __init__(self, token, loop):
        super().__init__(token, loop)

    async def _handler (self, message):
        if "event" in message['text']:
            events = await self.getData("FutureEvents")
            message_head = "Зараз в нас плануються такі івенти:"
            await self.sendMessage(message['chat']['id'], message_head)
            for event in events:
                await self.sendMessage(message['chat']['id'],
                                       self.MESSAGE_TEMPLATE.format(event['title'],
                                                                    event['date'],
                                                                    event['link'])
        elif "news" in message['text']:
            news = await self.getData("LastPosts")
            message_head = "Останні новини:"
            await self.sendMessage(message['chat']['id'], message_head)
            for post in news:
                await self.sendMessage(message['chat']['id'],
                                       self.MESSAGE_TEMPLATE.format(post['title'],
                                                                    post['date'],
                                                                    post['link'])
