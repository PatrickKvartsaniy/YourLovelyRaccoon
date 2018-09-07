import json
import aiohttp

from .bot import Conversation

class Raccoon(Conversation):
    def __init__(self, token, loop):
        super().__init__(token, loop)

    async def _handler (self, message):
        await self.sendMessage(message['chat']['id'],
                               message['text'])
