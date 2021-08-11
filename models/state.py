#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """attribute cities returns the list of City"""
            from models import storage
            from models.city import City
            c_list = []
            the_city = storage.all(City)
            for apart in the_city.values():
                if apart.state_id == self.id:
                    c_list.append(apart)
            return c_list