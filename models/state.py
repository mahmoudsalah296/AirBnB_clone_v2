#!/usr/bin/python3
""" State Module for HBNB project """
import models
import os
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """ cities getter attribute """
            cit_lis = []
            all_cit = models.storage.all(City)
            for city in all_cit.values():  # change .items() to values() as it
                # returns an obj that contains values of a dictionary as a list
                if city.state_id == self.id:
                    cit_lis.append(city)
            return cit_lis
