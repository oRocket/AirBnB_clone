#!/usr/bin/python3
"""A class User inherited from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User - A class representing a user in the application.

    Attributes:
    - id (str): A unique identifier for the User instance.
    - created_at (datetime): The datetime when the
                            User instance was created.
    - updated_at (datetime): The datetime when the
                            User instance was last updated.
    - email (str): The email address of the user.
    - password (str): The password associated with the user.
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.

    Methods:
    - __init__(self, *args, **kwargs): Initializes
                        a new instance of the User class.
    - __str__(self): Returns a string representation
                    of the User instance.

    Usage:
    - Create an instance of the User class: my_user = User()
    - Access attributes: my_user.id, my_user.created_at,
        my_user.updated_at, my_user.email, my_user.password,
        my_user.first_name, my_user.last_name
    - Convert to string: str(my_user)
    """
    def __init__(self, *args, **kwargs):
        '''
        Initializes a new instance of the User class.

        Args:
        - *args: Variable-length argument list.
        - **kwargs: Variable-length keyword argument list.

        If kwargs is not empty, the instance is
            created using the provided attributes.
        If kwargs is empty, a new instance
            is created with a new id and timestamps,
            and it is added to the storage.
        '''
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        '''
        Returns a string representation of the User instance.

        Example:
        "[User] (1234-5678) {'id': '1234-5678', 'created_at': datetime,
        'updated_at': datetime, 'email': 'user@example.com',
        'password': 'hashed_password',
        'first_name': 'John', 'last_name': 'Doe'}"
        '''
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )
