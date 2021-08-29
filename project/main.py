from sanic import Sanic
from project.settings import Settings
from databases import Database
from project.routes import setup_routes
import os

from dotenv import load_dotenv

load_dotenv()

app = Sanic(__name__)


def setup_database():
    app.db = Database(os.getenv('DB_URL'))

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
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        debug=os.getenv('DEBUG'),
        auto_reload=os.getenv('DEBUG')
        )
