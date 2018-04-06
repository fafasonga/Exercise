from sqlalchemy.orm import sessionmaker

from model import *

engine = create_engine('sqlite:///data.db', echo=True, convert_unicode=True)

Base = declarative_base()

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("songa", "Password0")
session.add(user)
session.commit()

user = User("admin", "Password0")
session.add(user)
# session.commit()

user = User("fabrice", "Password0")
session.add(user)
# session.commit()

Base.metadata.create_all(bind=engine)
