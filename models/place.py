#!/ur/bin/python3

""" This module contains the place class"""

from .base_model import BaseModel


class Place(BaseModel):
    """

    The Place class

    Attributes:
        city_id (str): City's id
        user_id (str): User's id
        name (str): Name of the Place
        description(str): Description of the place
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum number of guests
        price_by_night (int): Price by night
        latitude (float): The latitude
        longitude (float): The longitude
        amenity_ids (list): List of Amenity.id

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
