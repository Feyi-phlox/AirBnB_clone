#!/usr/bin/python3
"""Unittest for HBNBCommand class-console
"""

from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(TestCase):
    """Test cases for HBNBCommand class
    """

    def setUp(self):
        """Set up test environment
        """
        self.cli = HBNBCommand()

    def tearDown(self):
        """Clean up after tests
        """
        self.cli = None

    def test_empty_line(self):
        """Test empty line input
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd('\n')
            self.assertEqual(mock_stdout.getvalue(), '')

    def test_create_command(self):
        """Test create command
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd('create BaseModel\n')
            self.assertTrue(mock_stdout.getvalue().strip())
            self.assertGreaterEqual(len(mock_stdout.getvalue()), 36)

    def test_create_command_with_invalid_class(self):
        """Test create command with invalid class name
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd('create InvalidClassName\n')
            self.assertEqual(mock_stdout.getvalue(),
                             "** class doesn't exist **\n")

    def test_create_command_without_class_name(self):
        """Test create command without class name
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd('create\n')
            self.assertEqual(mock_stdout.getvalue(),
                             "** class name missing **\n")

    def test_show_command(self):
        """Test show command
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd('show BaseModel\n')
            self.assertEqual(mock_stdout.getvalue(),
                             "** instance id missing **\n")

    def test_show_command_with_invalid_class(self):
        """Test show command with invalid class name
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd('show InvalidClassName 123\n')
            self.assertEqual(mock_stdout.getvalue(),
                             "** class doesn't exist **\n")

    def test_show_command_without_instance_id(self):
        """Test show command without instance ID
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.onecmd('show BaseModel\n')
            self.assertEqual(mock_stdout.getvalue(),
                             "** instance id missing **\n")


if __name__ == '__main__':
    unittest.main()
