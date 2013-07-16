import model
import csv
from sqlalchemy.orm import sessionmaker

# make sure you're in (env) first!!
# >>> # python -i seed.py
# >>> session = model.connect()
# >>> load_users(session)

def load_users(session):
    with open('seed_data/u.usertest', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        for row in reader:
            print row  

def load_movies(session):
    # use u.item
    pass

def load_ratings(session):
    # use u.data
    pass

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    pass

if __name__ == "__main__":
    s= model.connect()
    main(s)
 