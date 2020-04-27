import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model import Book
import csv

engine = create_engine(os.getenv("DATABASE_URL"))
db_session = scoped_session(sessionmaker(bind=engine))
print ("db===============================")

with open('books.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        new_book = Book(isbn=row[0], title=row[1], author = row[2], year = row[3])
        db_session.add(new_book)
        
db_session.commit()
db_session.close()




 