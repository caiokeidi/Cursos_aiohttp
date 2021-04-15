from aiohttp import web
from db_files import insert

async def post_curso(request):
    info = await request.json()
    inserindo = await insert.insert_curso(info)
    return web.Response(text=str(inserindo))