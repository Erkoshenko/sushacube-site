from aiohttp import web
from os import environ

async def handle(request):
    return web.Response(text="Alive!")

async def start_web():
    app = web.Application()
    
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(environ.get("PORT", 5000))
    site = web.TCPSite(runner, host="0.0.0.0", port=port)
    
    await site.start()
    
    print('✅ Веб-сервер успешно запустился.')
