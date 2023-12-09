#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_instance_attributes(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_id_generation(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at_updated_at(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_str_representation(self):
        obj = BaseModel()
        obj_str = str(obj)
        self.assertTrue(isinstance(obj_str, str))
        self.assertIn("[BaseModel]", obj_str)
        self.assertIn("'id':", obj_str)
        self.assertIn("'created_at':", obj_str)
        self.assertIn("'updated_at':", obj_str)

if __name__ == '__main__':
    unittest.main()
