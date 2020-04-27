from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Integer, String

db = SQLAlchemy()



class Book(db.Model):
    __tablename__ = "BOOKS"
    isbn = db.Column(db.String, primary_key = True)
    title = db.Column(db.String, nullable = False)
    author = db.Column(db.String, nullable = False)
    publicationyear = db.Column(db.Integer, nullable = False)

    def __init__(self, isbn, title, author, publicationyear):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publicationyear = publicationyear

# db.create_all()
def __repr__(self):
     return '<Book %r>' % (self.name)
