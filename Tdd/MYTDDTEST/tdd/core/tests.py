# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .calc import add, subtract
from django.test import TestCase

# Create your tests here.


class CalcTest(TestCase):
    def test_add(self):
        """Just a simple add unity test"""
        self.assertEqual(add(2, 10), 12)

    def test_subtract(self):
        """Just a simple subtract unity test"""
        self.assertEqual(subtract(10, 2), 8)