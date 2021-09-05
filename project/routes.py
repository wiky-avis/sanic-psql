from project.tables import Book
from sanic.response import json
from sqlalchemy import create_engine, select

engine = create_engine('postgresql://sanic:sanic@localhost:5432', echo=True)


def setup_routes(app):
    @app.route('/')
    async def hello_world(request):
        return json({'hello': 'Hello world!'})

    @app.route('/books')
    async def book_list(request):
        with engine.connect() as conn:
            books = select(Book)
            data = conn.execute(books).fetchall()
            books= [dict(u) for u in data]
            return json({'books': books})
            #return jinja.render('hello.html', request, page=books)
