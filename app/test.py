"""
Sample Test
"""
from django.test import SimpleTestCase

from app import calc


class calcTest(SimpleTestCase):
    """ Test calc Functions """ 

    def test_add_numbers(self):
        result = calc.add(5, 6)
        self.assertEqual(result, 11)

