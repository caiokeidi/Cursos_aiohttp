from aiohttp import web
from views.get import get_todos_cursos

def add_urls(app):
    app.add_routes([
        web.get('/', get_todos_cursos)
    ])