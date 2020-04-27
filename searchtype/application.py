import os
import logging
import hashlib
from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from model import Book


# from bookimport import Book


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
print("db====================")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
print("db====================")
logging.debug("db sessions created")


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        isbn=request.form.get("isbn")
        title=request.form.get("title")
        author=request.form.get("author")
        year=request.form.get("year")
        req = request.form.get('search')
        data='%{}%'.format(req)
        print(Book.query.get("title"))
        if isbn:
            db.query(Book).filter(Book.isbn.like(data)).order_by(Book.title).all().fetchall()
        if title:
           data = db.query(Book).filter(Book.title.like(data)).order_by(Book.title).all().fetchall()
        if author:
            # print(searchparm)
            data= db.query(Book).filter(Book.author.like(data)).order_by(Book.title).fetchall()
        if year:
            data = db.query(Book).filter(Book.year.like(data)).order_by(Book.title).fetchall()
        if not data:
            return render_template("search.html", msg="0 records matched")
        else:
            return render_template("search.html", dat=data)


# @app.route("/book/<string:isbn>")
# def book_api(isbn):
#     return render_template("isbnvar.html", isbn=isbn)




            





           
