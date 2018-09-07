import asyncio
import aiohttp
import json

from aiohttp import web

from setup import init_app
from bot import Raccoon
from middleware import middleware_factory

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        app = loop.run_until_complete(init_app(loop))
        raccoon_bot = Raccoon(app['config']['telegram']['token'], loop)
        app.router.add_route('POST', '/api/v1/echo', raccoon_bot.handler)

        app.middlewares.append(middleware_factory)
        web.run_app(app,host='0.0.0.0',port=23456)
    except Exception as e:
        print(f"Error run server {e}")
    finally:
        loop.close()
        print("\nServer shut down")
