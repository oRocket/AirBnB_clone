#!/usr/bin/python3
""" A class State inherited from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State - A class representing a state in the application.

    Attributes:
    - id (str): A unique identifier for the State instance.
    - created_at (datetime): The datetime when the
                            State instance was created.
    - updated_at (datetime): The datetime when the
                            State instance was last updated.
    - name (str): The name of the state.

    Methods:
    - __init__(self, *args, **kwargs): Initializes a
                    new instance of the State class.
    - __str__(self): Returns a string representation
                    of the State instance.

    Usage:
    - Create an instance of the State class: my_state = State()
    - Access attributes: my_state.id, my_state.created_at,
                        my_state.updated_at, my_state.name
    - Convert to string: str(my_state)
    """
    def __init__(self, *args, **kwargs):
        '''
        Initializes a new instance of the State class.

        Args:
        - *args: Variable-length argument list.
        - **kwargs: Variable-length keyword argument list.

        If kwargs is not empty, the instance is
                created using the provided attributes.
        If kwargs is empty, a new instance is
                created with a new id and timestamps,
                and it is added to the storage.
        '''
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        '''
        Returns a string representation of the State instance.

        Example:
        "[State] (1234-5678) {'id': '1234-5678',
        'created_at': datetime, 'updated_at': datetime,
        'name': 'California'}"
        '''
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )
