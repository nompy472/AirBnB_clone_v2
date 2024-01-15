#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
STRG = os.environ.get('HBNB_TYPE_STORAGE')
>>>>>>> 489495ab7fb486e594c64433484868044f5de5e9


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
=======
    if STRG == 'db':
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'))
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""
>>>>>>> 489495ab7fb486e594c64433484868044f5de5e9
