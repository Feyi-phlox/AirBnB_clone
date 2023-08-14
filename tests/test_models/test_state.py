#!/usr/bin/python3

"""
Unittest module for State class
"""

import unittest
from models.state import State
from datetime import datetime
from unittest.mock import patch


class TestState(unittest.TestCase):
    """
    Test cases for State class
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.state = State()
        self.state.name = "test_name"

    def tearDown(self):
        """
        Clean up after tests
        """
        pass

    def test_module_doc(self):
        """Test module documentation"""
        doc = __import__("models.state").__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """Test class documentation"""
        doc = State.__doc__
        self.assertGreater(len(doc), 1)

    def test_init(self):
        """Test init method"""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertEqual(self.state.name, "test_name")

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test save method"""
        self.state.save()
        self.assertIsInstance(self.state.updated_at, datetime)
        mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """Test to_dict method"""
        obj_dict = self.state.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('name', obj_dict)

        self.assertIsInstance(obj_dict['id'], str)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertIsInstance(obj_dict['__class__'], str)
        self.assertEqual(obj_dict['name'], "test_name")


if __name__ == '__main__':
    unittest.main()
