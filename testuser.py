import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///credential.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("user", "pass")
session.add(user)


# commit the record the database
session.commit()
