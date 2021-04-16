from aiohttp import web
from db_files.delete_db import deleta_curso_db

async def deleta_curso(request):
    id = request.match_info['id']
    deleta = await deleta_curso_db(id)
    return web.Response(text=f'Objeto {id} processado: {deleta}')