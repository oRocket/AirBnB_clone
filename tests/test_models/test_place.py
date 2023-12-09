#!/usr/bin/python3

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_place_instance(self):
        """Test the creation of a Place instance."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_attributes(self):
        """Test Place attributes."""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, '')
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertEqual(place.user_id, '')
        # Add more attribute tests as needed

    def test_place_str_method(self):
        """Test the __str__ method of Place."""
        place = Place()
        place.name = 'Cozy Apartment'
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)

if __name__ == '__main__':
    unittest.main()
