from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Table, MetaData, join
from sqlalchemy.orm import mapper

engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False))

metadata = MetaData()

# after deleting to repopulate tables, delete ratings.db and run "python -i model.py"
# >> engine = create_engine("sqlite:///ratings.db", echo=True)

# to test:
# >>> python -i seed.py
# >>> session = model.connect()
# >>> load_users(session)

Base = declarative_base()
Base.query = session.query_property()

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def main():
    global session

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

    ratings = relationship("Rating", backref=backref("users", order_by=id))

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    name = Column(String(140), nullable=True)
    released_at = Column(DateTime, nullable=True)
    imdb_url = Column(String(140), nullable=True)

    ratings = relationship("Rating", backref=backref("movies", order_by=id))

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True) 
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id')) #ForeignKey('table.column_name')
    rating = Column(Integer, nullable=True)

    # user = relationship("User", backref=backref("ratings", order_by=id))

if __name__ == "__main__":
    main()