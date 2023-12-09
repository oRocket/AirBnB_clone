#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = 'file.json'
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_path_default(self):
        """Test the default file path."""
        self.assertEqual(self.storage._FileStorage__file_path, 'file.json')

    def test_objects_default(self):
        """Test the default objects attribute."""
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """Test the new method."""
        self.storage.new(self.base_model)
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save method."""
        self.storage.new(self.base_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            content = json.load(f)
            key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
            self.assertIn(key, content)

    def test_reload(self):
        """Test the reload method."""
        self.storage.new(self.base_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, new_storage.all())


if __name__ == '__main__':
    unittest.main()
