#!/usr/bin/python3

"""
Unittest module for Review class
"""

import unittest
from models.review import Review
from datetime import datetime
from unittest.mock import patch


class TestReview(unittest.TestCase):
    """
    Test cases for Review class
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.review = Review()
        self.review.place_id = "test_place_id"
        self.review.user_id = "test_user_id"
        self.review.text = "test_text"

    def tearDown(self):
        """
        Clean up after tests
        """
        pass

    def test_module_doc(self):
        """Test module documentation"""
        doc = __import__("models.review").__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """Test class documentation"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_init(self):
        """Test init method"""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertEqual(self.review.place_id, "test_place_id")
        self.assertEqual(self.review.user_id, "test_user_id")
        self.assertEqual(self.review.text, "test_text")

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test save method"""
        self.review.save()
        self.assertIsInstance(self.review.updated_at, datetime)
        mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """Test to_dict method"""
        obj_dict = self.review.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('place_id', obj_dict)
        self.assertIn('user_id', obj_dict)
        self.assertIn('text', obj_dict)

        self.assertIsInstance(obj_dict['id'], str)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertIsInstance(obj_dict['__class__'], str)
        self.assertEqual(obj_dict['place_id'], "test_place_id")
        self.assertEqual(obj_dict['user_id'], "test_user_id")
        self.assertEqual(obj_dict['text'], "test_text")


if __name__ == '__main__':
    unittest.main()
