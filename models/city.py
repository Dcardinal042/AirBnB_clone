#!/usr/bin/python3
"""
Module: city
City class for representing a city object
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Representation of a city.

    Attributes:
        if storage_t == 'db':
            __tablename__: Table name for the database storage.
            name: Column(String(128), nullable=False) - City name.
            state_id: Column(String(60), ForeignKey('states.id'),
                            nullable=False) # State ID.
            state: Relationship with State class.
            places: Relationship with Place class.
        else:
            state_id: Empty string for file storage.
            name: Empty string for file storage.

    Properties:
        state: Getter for the City's state instance.
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
        """
        Getter for the City's state instance.

        Returns:
            The State instance associated with this City.
        """
        return models.storage.get("State", self.state_id)
