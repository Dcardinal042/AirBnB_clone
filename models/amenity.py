#!/usr/bin/python3
"""
Module: amenity
Amenity class for representing an amenity object
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Representation of an amenity.

    Attributes:
        if storage_t == 'db':
            __tablename__: Table name for the database storage.
            name: Column(String(128), nullable=False) - Amenity name.
            place_amenities: relationship with PlaceAmenity class.
        else:
            name: Empty string for file storage.

    Properties:
        place_amenities: getter method for list of PlaceAmenity instances.
    """

    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("PlaceAmenity", backref="amenity")
    else:
        name = ""

    @property
    def place_amenities(self):
        """
        Getter for the list of PlaceAmenity instances related to this Amenity.

        Returns:
            A list of PlaceAmenity instances.
        """
        place_amenity_list = []
        all_place_amenities = models.storage.all("PlaceAmenity")
        for place_amenity in all_place_amenities.values():
            if place_amenity.amenity_id == self.id:
                place_amenity_list.append(place_amenity)
        return place_amenity_list
