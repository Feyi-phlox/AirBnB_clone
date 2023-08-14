#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Clean up after tests
        """
        pass

    def test_module_doc(self):
        """Test module documentation"""
        doc = __import__("models.base_model").__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """Test class documentation"""
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_init_doc(self):
        """Test init method documentation"""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_str_doc(self):
        """Test __str__ method documentation"""
        doc = BaseModel.__str__.__doc__
        self.assertGreater(len(doc), 1)

    def test_save_doc(self):
        """Test save method documentation"""
        doc = BaseModel.save.__doc__
        self.assertGreater(len(doc), 1)

    def test_to_dict_doc(self):
        """Test to_dict method documentation"""
        doc = BaseModel.to_dict.__doc__
        self.assertGreater(len(doc), 1)

    def test_init(self):
        """Test init method"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertIsInstance(self.base_model.created_at, datetime)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test save method"""
        self.base_model.save()
        self.assertIsInstance(self.base_model.updated_at, datetime)
        mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """Test to_dict method"""
        obj_dict = self.base_model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

        self.assertIsInstance(obj_dict['id'], str)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertIsInstance(obj_dict['__class__'], str)

    def test_init_kwargs(self):
        """Test init method with keyword arguments"""
        obj = BaseModel(
            id='test_id',
            created_at='2023-08-10T12:00:00.000000',
            updated_at='2023-08-10T13:00:00.000000',
            custom_attr='test'
        )

        self.assertEqual(obj.id, 'test_id')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.custom_attr, 'test')

    def test_overwrite_attributes(self):
        """Test overwriting attributes"""
        obj = BaseModel()
        obj.id = 'new_id'
        obj.name = 'Test'
        obj.custom_attr = 'custom_value'
        obj_dict = obj.to_dict()

        self.assertEqual(obj_dict['id'], 'new_id')
        self.assertEqual(obj_dict['name'], 'Test')
        self.assertEqual(obj_dict['custom_attr'], 'custom_value')


if __name__ == '__main__':
    unittest.main()
