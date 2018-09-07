import os
import json

import asyncio
import aiohttp

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
        host, port = '0.0.0.0', int(os.environ.get('PORT', 5000))
        web.run_app(app,host=host,port=port)
    except Exception as e:
        print(f"Error run server {e}")
    finally:
        loop.close()
        print("\nServer shut down")
