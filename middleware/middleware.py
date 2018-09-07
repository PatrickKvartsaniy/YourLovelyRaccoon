async def middleware_factory(app, handler):
    async def middleware_handler(request):
        data = await request.json()
        black_list = []
        if data['message']['from']['id'] in black_list:
            return web.Response(status=200)
        return await handler(request)
    return middleware_handler
