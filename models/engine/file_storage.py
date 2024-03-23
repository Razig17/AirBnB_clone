#!/usr/bin/python3
"""
This module contains class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""


import json
from models.base_model import BaseModel


class FileStorage():

    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    ___objects = {}

    def all(self):

        """ Returns the dictionary __objects"""
        return (self.___objects)

    def new(self, obj):

        """sets in __objects the obj with key <obj class name>.id"""

        self.___objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="UTF8") as file:
            json.dumps(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_as_dict = json.load(f)
                FileStorage.__objects = {
                    obj_id: eval(obj_dict["__class__"])(**obj_dict)
                    for obj_id, obj_dict in objects_as_dict.items()}
        except FileNotFoundError:
            pass
