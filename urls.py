from aiohttp import web
from views.get import get_todos_cursos
from views.post import post_curso

def add_urls(app):
    app.add_routes([
        web.get('/', get_todos_cursos),
        web.post('/insere/curso', post_curso)
    ])