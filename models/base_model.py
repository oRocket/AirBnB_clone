#!/usr/bin/python3
'''
Module for BaseModel class.
'''
from datetime import datetime
import uuid
import models


class BaseModel:
    '''
    BaseModel - The base class for all models in the application.

    Attributes:
    - id (str): A unique identifier for the instance.
    - created_at (datetime): The datetime when the instance was created.
    - updated_at (datetime): The datetime when the instance was last updated.

    Methods:
    - __init__(self, *args, **kwargs): Initializes a new instance
        of the BaseModel class.
    - __str__(self): Returns a string representation of the instance.
    - save(self): Updates the 'updated_at' attribute and
        saves the instance to the storage.
    - to_dict(self): Returns a dictionary representation of the instance.

    Usage:
    - Create an instance of the BaseModel class: my_instance = BaseModel()
    - Access attributes: my_instance.id, my_instance.created_at,
        my_instance.updated_at
    - Save changes: my_instance.save()
    - Convert to dictionary: my_instance.to_dict()

    Example:
    ```
    from models.base_model import BaseModel

    # Create a new instance
    my_instance = BaseModel()

    # Access attributes
    print(my_instance.id)
    print(my_instance.created_at)
    print(my_instance.updated_at)

    # Save changes
    my_instance.save()

    # Convert to dictionary
    my_dict = my_instance.to_dict()
    ```
    '''

    def __init__(self, *args, **kwargs):
        '''
        Initializes a new instance of the BaseModel class.

        Args:
        - *args: Variable-length argument list.
        - **kwargs: Variable-length keyword argument list.

        If kwargs is not empty, the instance is created
            using the provided attributes.
        If kwargs is empty, a new instance is created
            with a new id and timestamps, and it is added to the storage.
        '''
        if len(kwargs) != 0:
            """ Reconstruct the instance from the provided attributes """
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(
                    self.created_at,
                    "%Y-%m-%dT%H:%M:%S.%f"
                    )
            self.updated_at = datetime.strptime(
                    self.updated_at,
                    "%Y-%m-%dT%H:%M:%S.%f"
                    )
        else:
            """ Create a new instance with a new id and timestamps """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """ Add the new instance to the storage """
            models.storage.new(self)

    def __str__(self):
        '''
        Returns a string representation of the instance.

        Example:
        "[BaseModel] (1234-5678) {'id': '1234-5678',
            'created_at': datetime, 'updated_at': datetime}"
        '''
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        '''
        Updates the 'updated_at' attribute and
            saves the instance to the storage.
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        Returns a dictionary representation of the instance.

        Example:
        {'__class__': 'BaseModel', 'id': '1234-5678',
            'created_at': datetime, 'updated_at': datetime}
        '''
        copy_dict = self.__dict__.copy()
        copy_dict['__class__'] = self.__class__.__name__
        copy_dict['created_at'] = self.created_at.isoformat()
        copy_dict['updated_at'] = self.updated_at.isoformat()
        return copy_dict
