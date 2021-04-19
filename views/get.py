from aiohttp import web
from db_files.get_db import get_cursos_db, get_curso_db, get_cursos_nome_db
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

async def get_curso(request):
    id = request.match_info['id']
    curso = await get_curso_db(id)
    json_infos = json.dumps(dict(curso[0]), default=str)
    return web.Response(text=json_infos, content_type='application/json')

async def get_cursos_nome(request):
    nome = request.match_info['nome']
    cursos = await get_cursos_nome_db(nome)
    arr_cursos = []

    for curso in cursos:
        arr_cursos.append(dict(curso))
    
    json_cursos = json.dumps(arr_cursos, default=str)

    return web.Response(text=json_cursos, content_type='application/json')