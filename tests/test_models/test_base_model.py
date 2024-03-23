#!/usr/bin/python3
"""
 This module contains unittest for BaseModel Class
"""
import os
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):

    """Unittest for BaseModel"""

    def setUp(self):
        """Setup for the class"""
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Tear down for the class"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test for init"""
        tmp_model = BaseModel()

        self.assertIsNotNone(tmp_model.id)
        self.assertIsNotNone(tmp_model.created_at)
        self.assertIsNotNone(tmp_model.updated_at)

    def test_str(self):
        """Test for string representation"""
        tmp_model = BaseModel()

        self.assertTrue(str(tmp_model).startswith('[BaseModel]'))

        self.assertIn(tmp_model.id, str(tmp_model))

        self.assertIn(str(tmp_model.__dict__), str(tmp_model))

    def test_save(self):
        """Test for save method"""
        tmp_model = BaseModel()

        first_updated_at = tmp_model.updated_at

        new_updated_at = tmp_model.save()

        self.assertNotEqual(first_updated_at, new_updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        tmp_model = BaseModel()

        tmp_d = tmp_model.to_dict()

        self.assertIsInstance(tmp_d, dict)

        self.assertEqual(tmp_d["__class__"], 'BaseModel')
        self.assertEqual(tmp_d['id'], tmp_model.id)
        self.assertEqual(tmp_d['created_at'], tmp_model.created_at.isoformat())
        self.assertEqual(tmp_d["updated_at"], tmp_model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
