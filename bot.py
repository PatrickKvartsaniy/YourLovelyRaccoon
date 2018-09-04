import json
import asyncio
import aiohttp

from aiohttp import web

class Raccoon:
    def __init__(self,token,loop):
        self.token = token
        self.url = f"https://api.telegram.org/bot{self.token}/"
        self.loop = loop
        self.offset = None

    def __str__(self):
        return f"bot:{self.token}"

    async def get_updates(self,offset=None):
        params = {
            'timeout': 100,
            'offset': offset
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url + 'getUpdates', data=params) as resp:
                return await resp.json()

    async def get_last_update(self):
        json_data = await self.get_updates(self.offset)
        results = json_data['result']
        if len(results) > 0:
            last_update = results[-1]
        else:
            last_update = results[len(results)]
        return last_update

    async def send_msg(self,chat,text):
        params = {"chat_id":chat, "text":text}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url + 'sendMessage', data=params) as resp:
                return resp
    
    async def run(self):
        while 1:
            last_update = await self.get_last_update()
            message = last_update['message']['text']
            chat_id = last_update['message']['chat']['id']
            user_name = last_update['message']['chat']['first_name']

            await self.send_msg(chat_id,f"{user_name}:{message}")
            # print(f"Message from {chat_id} chat, {user_name}:{message}")

            self.offset = last_update['update_id'] + 1
