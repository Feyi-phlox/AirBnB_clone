#!/usr/bin/python3

"""
Unittest module for City class
"""

import unittest
from models.city import City
from datetime import datetime
from unittest.mock import patch


class TestCity(unittest.TestCase):
    """
    Test cases for City class
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.city = City()

    def tearDown(self):
        """
        Clean up after tests
        """
        pass

    def test_module_doc(self):
        """Test module documentation"""
        doc = __import__("models.city").__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """Test class documentation"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_init(self):
        """Test init method"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test save method"""
        self.city.save()
        self.assertIsInstance(self.city.updated_at, datetime)
        mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """Test to_dict method"""
        self.city.state_id = "1234"
        self.city.name = "lag"
        obj_dict = self.city.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('state_id', obj_dict)
        self.assertIn('name', obj_dict)

        self.assertIsInstance(obj_dict['id'], str)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertIsInstance(obj_dict['__class__'], str)
        self.assertIsInstance(obj_dict['state_id'], str)
        self.assertIsInstance(obj_dict['name'], str)


if __name__ == '__main__':
    unittest.main()
