#!/usr/bin/python3
""" A class Place inherited from BaseModel """
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place - A class representing a place in the application.

    Attributes:
    - id (str): A unique identifier for the Place instance.
    - created_at (datetime): The datetime when the
                            Place instance was created.
    - updated_at (datetime): The datetime when the
                            Place instance was last updated.
    - city_id (str): The ID of the city where the place is located.
    - user_id (str): The ID of the user who owns the place.
    - name (str): The name of the place.
    - description (str): A description of the place.
    - number_rooms (int): The number of rooms in the place.
    - number_bathrooms (int): The number of bathrooms in the place.
    - max_guest (int): The maximum number of guests
                        the place can accommodate.
    - price_by_night (int): The price per night for staying at the place.
    - latitude (float): The latitude coordinate of the place.
    - longitude (float): The longitude coordinate of the place.
    - amenity_ids (list): A list of amenity IDs
                        associated with the place.

    Methods:
    - __init__(self, *args, **kwargs): Initializes a
                    new instance of the Place class.
    - __str__(self): Returns a string representation
                    of the Place instance.

    Usage:
    - Create an instance of the Place class: my_place = Place()
    - Access attributes: my_place.id, my_place.created_at,
                my_place.updated_at, my_place.city_id,
                my_place.user_id, my_place.name, ...
    - Convert to string: str(my_place)
    """

    def __init__(self, *args, **kwargs):
        '''
        Initializes a new instance of the Place class.

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
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    def __str__(self):
        '''
        Returns a string representation of the Place instance.

        Example:
        "[Place] (1234-5678) {'id': '1234-5678', 'created_at': datetime,
        'updated_at': datetime, 'city_id': 'ABC',
        'user_id': 'DEF', 'name': 'Example Place', ...}"
        '''
        return '[{}] ({}) {}'.format(
                self.__class__.__name__
                self.id,
                self.__dict__
                )
