from aiohttp import web
from db_files.put_db import put_curso_db

async def put_curso(request):
    data = await request.json()
    atualizacao = await put_curso_db(data)
    return web.Response(text=f'Atualização de registro {data["id"]}: {atualizacao}')
