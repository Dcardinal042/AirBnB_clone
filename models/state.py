#!/usr/bin/python3

""" holds class State """

from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

if models.storage_t == "db":
    class State(BaseModel, Base):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
else:
    class State(BaseModel, Base):
        name = ""

    @property
    def cities(self):
        """getter for list of city instances related to the state"""
        city_list = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
