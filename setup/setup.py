import os
import json

from aiohttp import web

# BASE_DIR = os.path.dirname(__file__)

def install_config(app):
    with open("config.json") as c:
        config = json.load(c)
        app['config'] = config

async def init_app(loop):
    app = web.Application()
    install_config(app)
    return app
