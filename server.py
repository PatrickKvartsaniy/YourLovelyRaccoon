import asyncio

from bot import Raccoon

if __name__ == "__main__":
    token = "642399830:AAHfVtOjXl5TId9jlvTHqZmZhuSzz9TofKQ"
    loop = asyncio.get_event_loop()
    raccoon = Raccoon(token,loop)
    try:
        asyncio.ensure_future(raccoon.run())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
        loop.close()
    finally:
        loop.close()