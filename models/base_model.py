#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel():
    """
    A base class for models with common attributes and methods.
    """

    def __init__(self):
        """
        Constructor method for initializing a BaseModel object.
        """
        # Generate a unique identifier using UUID
        self.id = str(uuid.uuid4())
        
        # Set the creation and update timestamps to the current date and time
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the BaseModel object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the 'updated_at' timestamp to the current date and time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the BaseModel object to a dictionary.
        """
        ''' Create a copy of the object's dictionary attributes '''
        dict_copy = self.__dict__.copy()
        
        ''' Add additional information to the dictionary '''
        dict_copy["_class"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        
        return dict_copy

