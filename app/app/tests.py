from django.test import SimpleTestCase
from app import calc


class Test(SimpleTestCase):
    """ Test the Calc module. """

    def test_add_numbers(self):
        """ Testing adding numbers together """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ Testing subtracting numbers together """
        res = calc.subtract(5, 3)
        self.assertEqual(res, 2)
