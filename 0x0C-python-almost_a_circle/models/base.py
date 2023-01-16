#!/usr/bin/python3
# base.py

"""Define a Base class for all other classes in this project"""
import json

class Base():
    """Represents Base class"""
    __nb_objects = 0
    
    def __init__(self, id = None):
        """Initializes every instance of Base class

        Args
            id (int): ID value representing every instance created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON serialization of a list of dicts

        Args:
            list_dictionaries (list): a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
