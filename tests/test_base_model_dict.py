#!/usr/bin/python3
"""
Unittest for BaseModel dictionary instance
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelDict(unittest.TestCase):
    """Test BaseModel dictionary instance"""

    def setUp(self):
        """Set up test method"""
        self.base = BaseModel()
        self.base.name = "My_First_Model"
        self.base.my_number = 89

    def test_to_dict(self):
        """Test to_dict method of BaseModel"""
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(base_dict['name'], 'My_First_Model')
        self.assertEqual(base_dict['my_number'], 89)

    def test_to_dict_format(self):
        """Test the format of to_dict method"""
        base_dict = self.base.to_dict()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(datetime.strptime(base_dict['created_at'], date_format),
                         self.base.created_at)
        self.assertEqual(datetime.strptime(base_dict['updated_at'], date_format),
                         self.base.updated_at)

    def test_to_dict_output(self):
        """Test the output of to_dict method"""
        base_dict = self.base.to_dict()
        self.assertTrue(all(key in self.base.__dict__ for key in base_dict))

    def test_to_dict_instance_diff_from_class_input_output_equivalence(self):
        """Test input-output equivalence for instances of different classes"""
        base_dict = self.base.to_dict()
        new_base = BaseModel(**base_dict)
        new_base.name = "My_First_Model"
        new_base.my_number = 89
        self.assertEqual(self.base.id, new_base.id)
        self.assertEqual(self.base.created_at, new_base.created_at)
        self.assertEqual(self.base.updated_at, new_base.updated_at)
        self.assertEqual(self.base.name, new_base.name)
        self.assertEqual(self.base.my_number, new_base.my_number)
        self.assertNotEqual(self.base, new_base)

    def test_to_dict_output_is_dict(self):
        """Test if the output of to_dict method is a dictionary"""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)

    def test_to_dict_output_has_correct_class_key(self):
        """Test if the output of to_dict method has the correct class key"""
        base_dict = self.base.to_dict()
        self.assertIn("__class__", base_dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")

    def test_to_dict_output_has_correct_attributes(self):
        """Test if the output of to_dict method has the correct attributes"""
        base_dict = self.base.to_dict()
        expected_attrs = ["id", "created_at", "updated_at", "name", "my_number"]
        for attr in expected_attrs:
            self.assertIn(attr, base_dict)

    def test_to_dict_output_datetime_string(self):
        """Test if the datetime attributes are correctly formatted in the output"""
        base_dict = self.base.to_dict()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(datetime.strptime(base_dict["created_at"], date_format),
                         self.base.created_at)
        self.assertEqual(datetime.strptime(base_dict["updated_at"], date_format),
                         self.base.updated_at)

    def test_to_dict_method_with_additional_params(self):
        """Test to_dict method when passing additional parameters"""
        base_dict = self.base.to_dict(foo="bar", hello="world")
        self.assertIn("foo", base_dict)
        self.assertEqual(base_dict["foo"], "bar")
        self.assertIn("hello", base_dict)
        self.assertEqual(base_dict["hello"], "world")

    def test_to_dict_method_with_object_attributes(self):
        """Test to_dict method with an object that contains object attributes"""
        obj = ObjectWithAttributes()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["my_obj_attr"].__class__.__name__, "MyObjectAttribute")

    def test_to_dict_method_with_nested_object_attributes(self):
        """Test to_dict method with an object that contains nested object attributes"""
        obj = ObjectWithAttributes()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["nested_obj_attr"]["nested_attr"].__class__.__name__, "MyNestedObjectAttribute")


class ObjectWithAttributes:
    """A test class for to_dict tests"""

    def __init__(self):
        self.my_obj_attr = MyObjectAttribute()
        self.nested_obj_attr = {"nested_attr": MyNestedObjectAttribute()}


class MyObjectAttribute:
    """A test class for to_dict tests"""


class MyNestedObjectAttribute:
    """A test class for to_dict tests"""


if __name__ == "__main__":
    unittest.main()
