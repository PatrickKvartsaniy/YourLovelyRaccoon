import asyncio
import aiohttp

async def getData(api):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://aegee-website.herokuapp.com/api{api}/") as resp:
            print(resp)
            if resp.status == 200:
                data = await resp.json()
                return data
            else:
                print("Somthing went wrong, {resp.status}")

loop = asyncio.get_event_loop()

data = loop.run_until_complete(getData("FutureEvents"))

print(data)
