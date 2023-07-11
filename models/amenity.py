#!/usr/bin/python3
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of an amenity"""
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("PlaceAmenity", backref="amenity")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def place_amenities(self):
            """getter for list of PlaceAmenity instances"""
            place_amenity_list = []
            all_place_amenities = models.storage.all(PlaceAmenity)
            for place_amenity in all_place_amenities.values():
                if place_amenity.amenity_id == self.id:
                    place_amenity_list.append(place_amenity)
            return place_amenity_list
