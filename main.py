from aiohttp import web
from urls import add_urls


app = web.Application()

add_urls(app)

web.run_app(app)