from sanic.response import json
from project.tables import Book


def setup_routes(app):
    @app.route('/')
    async def hello_world(request):
        return json({'hello': 'Hello world!'})


def setup_routes(app):
    @app.route('/books')
    async def book_list(request):
        query = Book.select()
        rows = await request.app.db.fetch_all(query)
        return json({
            'books': [{row['title']: row['author']} for row in rows]
        })
