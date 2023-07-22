#!/usr/bin/python3
"""Module for State class."""

from models.base_model import BaseModel


class User(BaseModel):
    """User class for the user."""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
