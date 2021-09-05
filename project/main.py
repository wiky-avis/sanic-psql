import os

from databases import Database
from dotenv import load_dotenv
from project.routes import setup_routes
from project.settings import Settings
from sanic import Sanic

load_dotenv()

app = Sanic(__name__)


def setup_database():
    app.db = Database('postgresql://sanic:sanic@localhost:5432')

    @app.listener('after_server_start')
    async def connect_to_db(*args, **kwargs):
        await app.db.connect()

    @app.listener('after_server_stop')
    async def disconnect_from_db(*args, **kwargs):
        await app.db.disconnect()


def init():
    app.update_config(Settings)
    setup_database()
    setup_routes(app)
    app.run(
        host='localhost',
        port=8000,
        debug=True,
        auto_reload=True
        )
