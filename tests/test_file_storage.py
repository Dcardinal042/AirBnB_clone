#!/usr/bin/python3
"""
Contains the TestFileStorageDocs and TestFileStorage classes
"""

import unittest
import os
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""

    def test_module_docstring(self):
        """Tests for the presence of module docstring"""
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_class_docstring(self):
        """Tests for the presence of class docstring"""
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_methods_docstring(self):
        """Tests for the presence of methods docstring"""
        for method in dir(FileStorage):
            self.assertTrue(len(method.__doc__) > 0)

class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Tests the all() method of FileStorage"""
        obj_dict = self.storage.all()
        self.assertEqual(type(obj_dict), dict)
        self.assertIs(obj_dict, self.storage._FileStorage__objects)

    def test_new(self):
        """Tests the new() method of FileStorage"""
        obj_dict = self.storage.all()
        my_model = BaseModel()
        my_model.id = "12345"
        my_model.name = "My_Model"
        self.storage.new(my_model)
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIsNotNone(obj_dict.get(key))

    def test_save(self):
        """Tests the save() method of FileStorage"""
        obj_dict = self.storage.all()
        my_model = BaseModel()
        my_model.id = "12345"
        my_model.name = "My_Model"
        self.storage.new(my_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            file_content = f.read()
            self.assertIn("12345", file_content)
            self.assertIn("My_Model", file_content)

    def test_reload(self):
        """Tests the reload() method of FileStorage"""
        obj_dict = self.storage.all()
        my_model = BaseModel()
        my_model.id = "12345"
        my_model.name = "My_Model"
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIsNotNone(obj_dict.get(key))

    def test_datetime_deserialization(self):
        """Tests datetime deserialization"""
        my_model = BaseModel()
        my_model.created_at = datetime.utcnow()
        my_model.updated_at = datetime.utcnow()
        my_model_key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()
        obj_dict = self.storage.all()
        self.assertIn(my_model_key, obj_dict)
        loaded_model = obj_dict[my_model_key]
        self.assertEqual(type(loaded_model.created_at), datetime)
        self.assertEqual(type(loaded_model.updated_at), datetime)

if __name__ == '__main__':
    unittest.main()

