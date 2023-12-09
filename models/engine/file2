#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Class for serializing and deserializing objects to/from JSON file."""
    __file_path = "file.json"
    __objects = {}

    classes = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        serializable_objects = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(serializable_objects, f)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the file exists)."""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                json_objects = json.load(f)
            for key, value in json_objects.items():
                class_name, obj_id = key.split('.')
                class_obj = self.classes[class_name]
                self.__objects[key] = class_obj(**value)
        except FileNotFoundError:
            pass
