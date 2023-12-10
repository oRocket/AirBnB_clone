#!/usr/bin/python3

import unittest
import sys
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the command interpreter for testing."""
        self.console = HBNBCommand()
        sys.stdout = StringIO()

    def tearDown(self):
        """Clean up after the test."""
        sys.stdout = sys.__stdout__

    def test_quit_command(self):
        """Test the quit command."""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF_command(self):
        """Test the EOF command."""
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_create_command(self):
        """Test the create command."""
        self.console.onecmd("create BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output.isalnum())

    def test_show_command(self):
        """Test the show command."""
        base_model = BaseModel()
        base_model.save()
        obj_id = base_model.id
        self.console.onecmd(f"show BaseModel {obj_id}")
        output = sys.stdout.getvalue().strip()
        self.assertIn(obj_id, output)

    def test_destroy_command(self):
        """Test the destroy command."""
        base_model = BaseModel()
        base_model.save()
        obj_id = base_model.id
        self.console.onecmd(f"destroy BaseModel {obj_id}")
        all_objs = storage.all()
        self.assertNotIn(obj_id, all_objs)

    def test_all_command(self):
        """Test the all command."""
        self.console.onecmd("all")
        output = sys.stdout.getvalue().strip()
        self.assertFalse(output)

        self.console.onecmd("create BaseModel")
        self.console.onecmd("all BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertIn("BaseModel", output)

    def test_update_command(self):
        """Test the update command."""
        base_model = BaseModel()
        base_model.save()
        obj_id = base_model.id
        self.console.onecmd(f"update BaseModel {obj_id} name 'New Name'")
        base_model.reload()
        self.assertEqual(base_model.name, 'New Name')


if __name__ == '__main__':
    unittest.main()
