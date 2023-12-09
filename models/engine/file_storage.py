#!/bin/python3

import json
import models

class FileStorage():
  __file_path = "file.json"
  __objects = {}
  
  def all(self):
    return self.__objects
    
  def new(self, obj):
    key = f"{obj.__class__.__name__}.{obj.id}"
    self.__objects[key] = obj
  
  def save(self):
    with open(self.__file_path, "w", encoding="utf-8") as f:
        d = {k : v.to_dict() for k, v in self.__objects.items()}
        json.dump(d, f)
      
  def reload(self):
    try:
      with open(self.__file_path, "r", encoding="utf-8") as f:
              obj_dict = json.load(f)
              for o in obj_dict.values():
                clas_name = o["__class__"]
                del o["__class__"]
                self.new(eval(f"models.{clas_name}")(**o))
                
    except FileNotFoundError:
      return
