#!/usr/bin/python3
""" A class Review inherited from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review - A class representing a review in the application.

    Attributes:
    - id (str): A unique identifier for the Review instance.
    - created_at (datetime): The datetime when the
                            Review instance was created.
    - updated_at (datetime): The datetime when the
                            Review instance was last updated.
    - place_id (str): The ID of the place associated with the review.
    - user_id (str): The ID of the user who wrote the review.
    - text (str): The text content of the review.

    Methods:
    - __init__(self, *args, **kwargs): Initializes a new
                        instance of the Review class.
    - __str__(self): Returns a string representation
                        of the Review instance.

    Usage:
    - Create an instance of the Review class: my_review = Review()
    - Access attributes: my_review.id, my_review.created_at,
            my_review.updated_at, my_review.place_id,
            my_review.user_id, my_review.text
    - Convert to string: str(my_review)
    """
    def __init__(self, *args, **kwargs):
        '''
        Initializes a new instance of the Review class.

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
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def __str__(self):
        '''
        Returns a string representation of the Review instance.

        Example:
        "[Review] (1234-5678) {'id': '1234-5678', 'created_at': datetime,
        'updated_at': datetime, 'place_id': 'ABC',
        'user_id': 'DEF', 'text': 'Example Review Content'}"
        '''
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )
