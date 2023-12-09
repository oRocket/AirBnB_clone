#!/usr/bin/python3

import json
import os
from datetime import datetime

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    obj_data['__class__'] = class_name
                    obj_data['created_at'] = datetime.strptime(obj_data['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj_data['updated_at'] = datetime.strptime(obj_data['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj_class = globals().get(class_name)  # Using get to avoid NameError
                    if obj_class:
                        obj_instance = obj_class(**obj_data)
                        self.__objects[key] = obj_instance
