#!/usr/bin/python3

""" holds class City"""

from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

if models.storage_t == 'db':
    class City(BaseModel, Base):
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship("State", back_populates="cities")
        places = relationship("Place", backref="cities")
else:
    class City(BaseModel, Base):
        state_id = ""
        name = ""

    @property
    def state(self):
        """getter for City's state instance"""
        return models.storage.get(State, self.state_id)
