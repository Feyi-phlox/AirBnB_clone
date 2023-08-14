#!/usr/bin/python3

"""
Unittest module for Place class
"""

import unittest
from models.place import Place
from datetime import datetime
from unittest.mock import patch


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.place = Place()
        self.place.city_id = "test_city_id"
        self.place.user_id = "test_user_id"
        self.place.name = "test_name"
        self.place.description = "test_description"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = -122.4194
        self.place.amenity_ids = ["test_amenity_id"]

    def tearDown(self):
        """
        Clean up after tests
        """
        pass

    def test_module_doc(self):
        """Test module documentation"""
        doc = __import__("models.place").__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """Test class documentation"""
        doc = Place.__doc__
        self.assertGreater(len(doc), 1)

    def test_init(self):
        """Test init method"""
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertEqual(self.place.city_id, "test_city_id")
        self.assertEqual(self.place.user_id, "test_user_id")
        self.assertEqual(self.place.name, "test_name")
        self.assertEqual(self.place.description, "test_description")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.amenity_ids, ["test_amenity_id"])

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test save method"""
        self.place.save()
        self.assertIsInstance(self.place.updated_at, datetime)
        mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """Test to_dict method"""
        obj_dict = self.place.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('city_id', obj_dict)
        self.assertIn('user_id', obj_dict)
        self.assertIn('name', obj_dict)
        self.assertIn('description', obj_dict)
        self.assertIn('number_rooms', obj_dict)
        self.assertIn('number_bathrooms', obj_dict)
        self.assertIn('max_guest', obj_dict)
        self.assertIn('price_by_night', obj_dict)
        self.assertIn('latitude', obj_dict)
        self.assertIn('longitude', obj_dict)
        self.assertIn('amenity_ids', obj_dict)

        self.assertIsInstance(obj_dict['id'], str)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertIsInstance(obj_dict['__class__'], str)
        self.assertEqual(obj_dict['city_id'], "test_city_id")
        self.assertEqual(obj_dict['user_id'], "test_user_id")
        self.assertEqual(obj_dict['name'], "test_name")
        self.assertEqual(obj_dict['description'], "test_description")
        self.assertEqual(obj_dict['number_rooms'], 2)
        self.assertEqual(obj_dict['number_bathrooms'], 1)
        self.assertEqual(obj_dict['max_guest'], 4)
        self.assertEqual(obj_dict['price_by_night'], 100)
        self.assertEqual(obj_dict['latitude'], 37.7749)
        self.assertEqual(obj_dict['longitude'], -122.4194)
        self.assertEqual(obj_dict['amenity_ids'], ["test_amenity_id"])


if __name__ == '__main__':
    unittest.main()
