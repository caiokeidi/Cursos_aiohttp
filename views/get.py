from aiohttp import web
from db_files.get_db import get_cursos_db
import json

async def get_index(request):
    return web.Response(text='<h1>Página Inicial</h1><h2>Verifique com o administrador o correto uso dessa api</h2', content_type='text/html')

async def get_todos_cursos(request):
    infos = await get_cursos_db()
    
    arr_infos = []
    for info in infos:  
        dict_info = dict(info)
        arr_infos.append(dict_info)

    json_infos = json.dumps(arr_infos, default=str)
    return web.Response(text=json_infos, content_type='application/json')

