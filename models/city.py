#!/ur/bin/python3

""" This module contains the city class"""

from .base_model import BaseModel


class City(BaseModel):
    """

    The City class

    Attributes:
        state_id (str): The id of the State
        name (str): City's name

    """
    state_id = ""
    name = ""
