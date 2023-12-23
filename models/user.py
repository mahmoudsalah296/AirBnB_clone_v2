#!/usr/bin/python3

"""
A module that defines the ORM class for User table
"""
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Defines attributes for User table
    """
    __tablename__ = 'users'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            'Place', backref='user', cascade='all, delete')
        reviews = relationship(
            'Review', backref='user', cascade='all, delete')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
