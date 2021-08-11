#!/usr/bin/python3
"""database storage for hbnb clone"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv

class DBStorage:
    """Class Storage"""
    __engine = None
    __session = None

    def __init__(self):
         self.__engine = create_engine()

    def all(self, cls=None):()