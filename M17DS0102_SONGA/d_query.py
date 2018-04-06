from sqlalchemy.orm import sessionmaker
from model import *

engine = create_engine('sqlite:///data.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create objects
for val in session.query(User).order_by(User.id):
    print(val.username, val.password)
