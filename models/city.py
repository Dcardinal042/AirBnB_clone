#!/usr/bin/python3

""" holds class City"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """
    Representation of a city
    """
    if models.storage_t == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship("State", back_populates="cities")
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

        @property
        def state(self):
            """getter for City's state instance"""
            return models.storage.get("State", self.state_id)
