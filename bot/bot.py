import json

import asyncio
import aiohttp

from aiohttp import web

class Bot(object):
    TELEGRAM_URL = "https://api.telegram.org/bot{}/{}"
    HEROKU_URL = "https://aegee-website.herokuapp.com/api{}"

    def __init__(self, token, db, loop):
        self._token = token
        self._db = db
        self._loop = loop

    async def _request(self, method, message):
        headers = {
            "Content-type": "application/json"
        }
        async with aiohttp.ClientSession(loop=self._loop) as session:
            async with session.post(self.TELEGRAM_URL.format(self._token, method),
                                    data=json.dumps(message),
                                    headers=headers) as resp:
                try:
                    assert resp.status == 200
                except:
                    # return web.Response(status=500
                    pass
        return web.Response(status=200)

    async def getData(self, api):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.HEROKU_URL.format(api)) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    print("Somthing went wrong, {resp.status}")

    async def sendMessage(self, chatId, text):
        message = {
            'chat_id': chatId,
            'text': text
        }
        await self._request('sendMessage', message)

    async def save_sub(self, sub, id, first_name, username):
        subscriber = {"telegram_id": id,
                      "first_name": first_name,
                      "username": username}
        check = await self.db['subscribers'].find_one({"telegram_id":subscriber['id']})
        if check == None:
            await self.db['subscribers'].insert_one(subscriber)
            return "Done"
        return "Exist"


class Conversation(Bot):
    def __init__(self, token, db, loop):
        super().__init__(token, db, loop)

    async def _handler(self, message):
        pass

    async def handler(self, request):
        message = await request.json()
        asyncio.ensure_future(self._handler(message["message"]))
        return aiohttp.web.Response(status=200)
