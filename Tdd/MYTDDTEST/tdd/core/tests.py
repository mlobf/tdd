# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .calc import add
from django.test import TestCase

# Create your tests here.


class CalcTest(TestCase):
    def test_add(self):
        """Just a simple unity test"""
        self.assertEqual(add(2, 10), 12)
