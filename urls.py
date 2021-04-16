from aiohttp import web
from views.get import get_todos_cursos, get_index
from views.post import post_curso
from views.delete import deleta_curso

def add_urls(app):
    app.add_routes([
        web.get('/', get_index),
        web.get('/cursos', get_todos_cursos),
        web.post('/insere/curso', post_curso),
        web.delete('/deleta/curso/{id}', deleta_curso)
    ])