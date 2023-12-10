#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """
    City - A class representing a city in the application.

    Attributes:
    - id (str): A unique identifier for the City instance.
    - created_at (datetime): The datetime when the
                            City instance was created.
    - updated_at (datetime): The datetime when the
                            City instance was last updated.
    - state_id (str): The ID of the state to which the city belongs.
    - name (str): The name of the city.

    Methods:
    - __init__(self, *args, **kwargs): Initializes
                a new instance of the City class.
    - __str__(self): Returns a string representation
                of the City instance.

    Usage:
    - Create an instance of the City class: my_city = City()
    - Access attributes: my_city.id, my_city.created_at,
                my_city.updated_at, my_city.state_id, my_city.name
    - Convert to string: str(my_city)
    """

    def __init__(self, *args, **kwargs):
        '''
        Initializes a new instance of the City class.

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
        self.state_id = ""
        self.name = ""

    def __str__(self):
        '''
        Returns a string representation of the City instance.

        Example:
        "[City] (1234-5678) {'id': '1234-5678',
            'created_at': datetime,
            'updated_at': datetime,
            'state_id': 'ABC',
            'name': 'Example City'}"
        '''
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )
