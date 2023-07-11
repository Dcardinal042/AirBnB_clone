#!/usr/bin/python3
"""
Contains the FileStorage class
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls is None:
            return self.__objects

        cls_name = cls if isinstance(cls, str) else cls.__name__
        filtered_objects = {
            key: obj for key, obj in self.__objects.items()
            if isinstance(obj, classes[cls_name])
        }
        return filtered_objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        json_objects = {}
        for key, obj in self.__objects.items():
            json_objects[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(json_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                json_objects = json.load(file)

            for key, json_data in json_objects.items():
                class_name, obj_id = key.split(".")
                cls = classes[class_name]
                obj = cls(**json_data)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects.pop(key, None)

    def close(self):
        self.reload()


classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

