#!/usr/bin/python3

"""
This module contains BaseModule class that
defines all common attributes/methods for other classes
"""

from datetime import datetime
import models
import uuid


class BaseModel():

    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize instances of the BaseModel class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:

            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns [<class name>] (<self.id>) <self.__dict__>"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict
