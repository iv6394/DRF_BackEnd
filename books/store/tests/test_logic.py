import imp
from unittest import TestCase


from django.test import TestCase
from store.logic import operations

class LogicTestCase(TestCase):
    
    def test_plus(self):
        result = operations(7, 13, '+')
        self.assertEqual(20, result)

    def test_minus(self):
        result = operations(27, 13, '-')
        self.assertEqual(14, result)

    def test_multiply(self):
        result = operations(7, 13, '*')
        self.assertEqual(91, result)