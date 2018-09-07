import json
import aiohttp

from .bot import Conversation

class Raccoon(Conversation):
    def __init__(self, token, loop):
        super().__init__(token, loop)

    async def _handler (self, message):
        if "/events" in message['text']:
            data = await self.getData("FutureEvents")
            message_text = f"""Зараз в нас плануються такі івенти: /n
                              {data[0]['title']}, посилання - {data[0]['link']}"""
            await self.sendMessage(message['chat']['id'],)
