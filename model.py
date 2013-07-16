from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

# to test:
# >>> python -i seed.py
# >>> session = model.connect()
# >>> load_users(session)

Base = declarative_base()

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def main():
    """In case we need this for something"""
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    name = Column(String(140), nullable=True)
    released_at = Column(DateTime, nullable=True)
    imdb_url = Column(String(140), nullable=True)

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)  
    movie_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    rating = Column(Integer, nullable=True)


if __name__ == "__main__":
    main()
