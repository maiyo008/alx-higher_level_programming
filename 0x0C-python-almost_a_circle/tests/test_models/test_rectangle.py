#!/usr/bin/python3
# test_rectangle.py

"""Defines unittests for models/rectangle.py

Unittest classes:
    TestRectangle_instatiation

"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_instatiation(unittest.TestCase):
    """Unittests for testing  instatiation of the Rectangle class"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 1), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_two_args(self):
        r1 = Rectangle(3,6)
        r2 = Rectangle(75,53)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(23,34,53,2)
        r2 = Rectangle(5,6,2,7)
        self.assertEqual(r1.id, r2.id - 1)
    def test_five_args(self):
        self.assertEqual(3, Rectangle(3,5,6,7,3).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(3,2,4,5,63,6,7)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5,2,4,5,7).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3,5,7,2,5).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_setter(self):
        r = Rectangle(4,5,6,3,6)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)

