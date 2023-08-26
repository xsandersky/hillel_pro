import sqlalchemy as db
from sqlalchemy import create_engine
import uuid
engine = create_engine('sqlite:///books.db')

connection = engine.connect()

metadata = db.MetaData()

books = db.Table('books', metadata,
                 db.Column('id', db.Integer, primary_key=True),
                 db.Column('name', db.String),
                 db.Column('author', db.String),
                 db.Column('date_of_realese', db.Date),
                 db.Column('description', db.String),
                 db.Column('genre', db.String))

metadata.create_all(engine)

insertation_query = books.insert().values(
    {"name": "Alphabet", "author": "Ivan Fedorov", "date_of_realese": '05.05.1574',
     "description": "All literals", "genre": "for child"}
)

connection.execute(insertation_query)

# select_all_query = db.select(books)
# select_all_result = connection.execute(select_all_query)
#
# print(select_all_result.fetchall())