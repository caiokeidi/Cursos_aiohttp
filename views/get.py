from aiohttp import web

async def get_todos_cursos(request):
    return web.Response(text='teste')
