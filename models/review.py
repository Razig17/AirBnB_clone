#!/ur/bin/python3

""" This module contains the review class"""

from .base_model import BaseModel


class Review(BaseModel):
    """

    The Review class

    Attributes:
        place_id (str): The id of the place
        user_id (str): User's id
        text (str): Review text

    """
    place_id = ""
    user_id = ""
    text = ""
