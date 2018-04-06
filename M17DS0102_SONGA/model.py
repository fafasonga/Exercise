from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
import datetime
from sqlalchemy import *
import json


engine = create_engine('sqlite:///data.db', echo=True)

Base = declarative_base()

# creating the template for our Database
# creating the template for our Database

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.__str__()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255), index=True, unique=True)
    password = Column(String(255), index=True, unique=True)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "ID: {}. username: {}. password: {}.".format(self.id, self.username, self.password)


# create tables
Base.metadata.create_all(engine)
