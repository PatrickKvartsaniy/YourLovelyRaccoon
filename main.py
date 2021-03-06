import os
import json

import asyncio
import aiohttp

from aiohttp import web

from setup import init_app, init_mongo
from bot import Raccoon
from middleware import middleware_factory

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        app = loop.run_until_complete(init_app(loop))
        db = loop.run_until_complete(init_mongo(app['config']['mongo']))

        raccoon_bot = Raccoon(app['config']['telegram']['token'], db, loop)

        app.router.add_routes([web.post('/api/v1/echo', raccoon_bot.handler),
                               web.post('/dispatcher', raccoon_bot.dispatcher)])

        app.middlewares.append(middleware_factory)
        host, port = '0.0.0.0', int(os.environ.get('PORT', 5000))
        web.run_app(app,host=host,port=port)
    # except Exception as e:
    #     print(f"Error run server {e}")
    finally:
        loop.close()
        print("\nServer shut down")
