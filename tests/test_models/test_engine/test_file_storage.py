#!/usr/bin/python3


"""
 This module contains unittest for FileStorage Class
"""
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittest for  file storage class"""

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):

        with self.assertRaises(TypeError):
            models.storage.new()

        my_model = BaseModel()
        models.storage.new(my_model)

        self.assertIn(my_model, models.storage.all().values())

        self.assertIn(f"BaseModel.{my_model.id}", models.storage.all().keys())

    def test_new_more_than_one_arg(self):
        b1 = BaseModel()
        b2 = BaseModel()
        with self.assertRaises(TypeError):
            models.storage.new(b1, b2)

    def test_save(self):
        my_base_model = BaseModel()

        models.storage.save()
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + my_base_model.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        my_base_model = BaseModel()

        models.storage.new(my_base_model)

        models.storage.save()
        models.storage.reload()

        objs = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + my_base_model.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
