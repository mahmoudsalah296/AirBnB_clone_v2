#!/usr/bin/python3

"""
A module that defines extensively the database storage for this project
"""
from os import getenv
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """Database utilities definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Makes a query to the database
        if cls is given, query for cls only else query for all"""
        objs = []
        if cls is None:
            Classes = [User, City, State, Place, Review, Amenity]
            try:
                for Class in Classes:
                    objs = objs + self.__session.query(Class).all()
            except Exception:
                pass
        else:
            Class = eval(cls) if type(cls) == str else cls
            objs = self.__session.query(Class).all()
        return {'{}.{}'.format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Dispose of the current Session, if present."""
        self.__session.close()
