import json
import aiohttp

from .bot import Conversation

class Raccoon(Conversation):
    def __init__(self, token, loop):
        super().__init__(token, loop)

    async def _handler (self, message):
        if "events" in message['text']:
            events = await self.getData("FutureEvents")
            message_head = "Зараз в нас плануються такі івенти:"
            await self.sendMessage(message['chat']['id'], message_head)
            for event in data:
                await self.sendMessage(message['chat']['id'], f"{data[0]['title']}, посилання - {data[0]['link']}")
