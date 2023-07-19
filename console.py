#!/usr/bin/python3
<<<<<<< HEAD
"""
BaseModel class that defines all common attributes/methods for other classes
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from re import search


class HBNBCommand(cmd.Cmd):
    """
        Summary: class that define the command interpreter:
    """
    prompt = "(hbnb) "
    list_classes = ["BaseModel", "User", "Place", "State", "City",
                    "Amenity", "Review"]

    doc_header = "Documented commands (type help <topic>):"
    ruler = '='

    def do_EOF(self, line):
        "Exit the program with Ctrl+D"   
