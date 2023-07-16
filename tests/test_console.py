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

    # ... (rest of the test cases)

    def test_update_missing_attr_value(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 123")
            self.assertEqual(f.getvalue().strip(), "** value missing **")


if __name__ == '__main__':
    unittest.main()
