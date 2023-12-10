#!/usr/bin/python3
""" A class FileStorage Module """

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''
    FileStorage - A class responsible for serializing
                    and deserializing instances.

    Attributes:
    - __file_path (str): The path to the JSON file
                        for storing serialized instances.
    - __objects (dict): A dictionary to store serialized instances.

    Methods:
    - all(self): Returns the dictionary __objects.
    - new(self, obj): Adds a new instance to the __objects dictionary.
    - save(self): Serializes and saves instances to the JSON file.
    - reload(self): Deserializes instances from the
                        JSON file and updates __objects.
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """ Adds a new instance to the __objects dictionary. """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes and saves instances to the JSON file. """
        new_dict = {}
        with open(self.__file_path, mode='w+', encoding='utf-8') as file:
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes instances from the JSON file and updates __objects"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                new_objects = json.load(file)
                for key, value in new_objects.items():
                    class_name = value['__class__']
                    reloaded_object = eval('{}(**value)'.format(class_name))
                    self.__objects[key] = reloaded_object

        except IOError:
            pass
