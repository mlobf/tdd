from django.test import TestCase
from core.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)

    def test_sub_numbers(self):
        self.assertEqual(subtract(2, 8), 6)
