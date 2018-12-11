from aiohttp import web
import aiohttp_jinja2
import jinja2

from db import init_pg, close_pg
from settings import config
from routes import setup_routes

app = web.Application()
setup_routes(app)
app['config'] = config
aiohttp_jinja2.setup(
    app, loader=jinja2.PackageLoader('aiohttpdemo_polls', 'templates'))
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app)
