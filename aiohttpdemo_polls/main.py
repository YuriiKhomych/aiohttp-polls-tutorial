import logging

from aiohttp import web
import aiohttp_jinja2
import jinja2

from aiohttpdemo_polls.db import init_pg, close_pg
from aiohttpdemo_polls.middlewares import setup_middlewares
from aiohttpdemo_polls.routes import setup_routes
from aiohttpdemo_polls.settings import config


async def init_app():
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('aiohttpdemo_polls', 'templates'))
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    setup_routes(app)
    setup_middlewares(app)
    return app


def main():
    logging.basicConfig(level=logging.DEBUG)

    app = init_app()

    web.run_app(app)


if __name__ == '__main__':
    main()
