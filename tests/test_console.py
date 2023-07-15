#!/usr/bin/python3
"""
Unittests for console.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
import models
from models.base_model import BaseModel
from models.state import State
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_success(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertTrue(obj_id)

    def test_show_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_show_success(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertTrue(obj_id)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(obj_id))
            self.assertIn(obj_id, f.getvalue().strip())

    def test_destroy_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_success(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertTrue(obj_id)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            self.assertEqual(f.getvalue().strip(), "")

    def test_all_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_all_success(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertTrue(obj_id)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertIn(obj_id, f.getvalue().strip())

    def test_update_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel invalid_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attr_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel {}".format("123"))
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

    def test_update_missing_attr_value(self):
        with patch('sys.stdout', new
