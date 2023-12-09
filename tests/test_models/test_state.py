#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_state_instance(self):
        """Test the creation of a State instance."""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_attributes(self):
        """Test State attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, '')

    def test_state_str_method(self):
        """Test the __str__ method of State."""
        state = State()
        state.name = 'California'
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)


if __name__ == '__main__':
    unittest.main()
