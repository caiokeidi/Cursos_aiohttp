from aiohttp import web
from views.get import get_todos_cursos, get_index, get_curso
from views.post import post_curso
from views.delete import deleta_curso
from views.put import put_curso

def add_urls(app):
    app.add_routes([
        web.get('/', get_index),
        web.get('/cursos', get_todos_cursos),
        web.get('/curso/{id}', get_curso),
        web.post('/insere/curso', post_curso),
        web.put('/atualiza/curso', put_curso),
        web.delete('/deleta/curso/{id}', deleta_curso)
    ])