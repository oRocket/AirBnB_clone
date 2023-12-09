#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity_instance(self):
        """Test the creation of an Amenity instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_attributes(self):
        """Test Amenity attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')

    def test_amenity_str_method(self):
        """Test the __str__ method of Amenity."""
        amenity = Amenity()
        amenity.name = 'WiFi'
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

if __name__ == '__main__':
    unittest.main()
