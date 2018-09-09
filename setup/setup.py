import os
import json

from aiohttp import web
import motor.motor_asyncio
# BASE_DIR = os.path.dirname(__file__)

def install_config(app):
    with open("config.json") as c:
        config = json.load(c)
        app['config'] = config

async def init_app(loop):
    app = web.Application()
    install_config(app)
    return app

async def init_mongo(config):
    client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['db']}")
    db = client['aegee']
    return db
