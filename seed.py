import model
import csv
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# make sure you're in (env) first!!
# >>> # python -i seed.py
# >>> session = model.connect()
# >>> load_users(session)

def load_users(session):
    with open('seed_data/u.user', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        for row in reader:
            id = row[0]
            age = row[1]
            zipcode = row[4]
            u = model.User(id=id, age=age, zipcode=zipcode)
            session.add(u)
        session.commit()

def load_movies(session):
    with open('seed_data/u.item', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        for row in reader:
            id = row[0]
            name = row[1]
            name = name.decode("latin-1")
            if row[2] == '':
                r = None
            else: 
                r = datetime.strptime(row[2], "%d-%b-%Y")
            imdb_url = row[3]
            u = model.Movie(id=id, name=name, released_at=r, imdb_url=imdb_url)
            session.add(u)
        session.commit()

def load_ratings(session):
    with open('seed_data/u.data', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            user_id = row[0]
            movie_id = row[1]
            rating = row[2]
            u = model.Rating(user_id=user_id, movie_id=movie_id, rating=rating)
            session.add(u)
        session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    # load_users(session) # comment this out when seed users have been loaded
    # load_movies(session) # comment this out when seed movies have been loaded
    # load_ratings(session) # comment this out when seed ratings have been loaded

if __name__ == "__main__":
    s= model.connect()
    main(s)
 