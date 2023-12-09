#!/usr/bin/python3

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_review_instance(self):
        """Test the creation of a Review instance."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        """Test Review attributes."""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, '')
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, '')
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, '')
        # Add more attribute tests as needed

    def test_review_str_method(self):
        """Test the __str__ method of Review."""
        review = Review()
        review.text = 'Great experience!'
        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected_str)

if __name__ == '__main__':
    unittest.main()
