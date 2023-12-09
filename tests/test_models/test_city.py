#!/usr/bin/python3

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_city_instance(self):
        """Test the creation of a City instance."""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        """Test City attributes."""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, '')
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, '')

    def test_city_str_method(self):
        """Test the __str__ method of City."""
        city = City()
        city.name = 'San Francisco'
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)


if __name__ == '__main__':
    unittest.main()
