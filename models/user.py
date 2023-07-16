#!/usr/bin/python3
"""
User class module
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Representation of a user
    """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
                "Place", backref="user", cascade="all, delete-orphan"
                )
        reviews = relationship(
                "Review", backref="user", cascade="all, delete-orphan"
                )
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes user
        """
        super().__init__(*args, **kwargs)

    # Implement additional methods or properties here

    # Example implementation of a new method
    def full_name(self):
        """
        Returns the full name of the user
        """
        return f"{self.first_name} {self.last_name}"

    # Update existing methods if necessary

    def __str__(self):
        """
        Returns a string representation of the user
        """
        return f"[User] ({self.id}) {self.email}: {self.full_name()}"
