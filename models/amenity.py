#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity - A class representing an amenity in the application.

    Attributes:
    - id (str): A unique identifier for the Amenity instance.
    - created_at (datetime): The datetime when
                            the Amenity instance was created.
    - updated_at (datetime): The datetime when
                            the Amenity instance was last updated.
    - name (str): The name of the amenity.

    Methods:
    - __init__(self, *args, **kwargs): Initializes a new
                                    instance of the Amenity class.
    - __str__(self): Returns a string representation of the Amenity instance.

    Usage:
    - Create an instance of the Amenity class: my_amenity = Amenity()
    - Access attributes: my_amenity.id, my_amenity.created_at,
                        my_amenity.updated_at, my_amenity.name
    - Convert to string: str(my_amenity)
    """

    def __init__(self, *args, **kwargs):
        '''
        Initializes a new instance of the Amenity class.

        Args:
        - *args: Variable-length argument list.
        - **kwargs: Variable-length keyword argument list.

        If kwargs is not empty, the instance
                is created using the provided attributes.
        If kwargs is empty, a new instance
                is created with a new id and timestamps,
        and it is added to the storage.
        '''
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        '''
        Returns a string representation of the Amenity instance.

        Example:
        "[Amenity] (1234-5678) {'id': '1234-5678',
            'created_at': datetime, 'updated_at': datetime,
            'name': 'Example Name'}"
        '''
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id, self.__dict__
                )
