__author__ = 'themanda'
import unittest
from factory import *


class FactoryTests(unittest.TestCase):

    def test_raises_arguments(self):
        """testing of assert the exception if receive some missing arguments"""
        self.assertRaises(ArgumentError, factorize)
        self.assertRaises(ArgumentError, factorize, module='factory')
        self.assertRaises(ArgumentError, factorize, object_type='UnknownClass')

    def test_raises_unknown_class(self):
        self.assertRaises(NonExistentTypeError, factorize, module='factory', object_type='UnknownClass')

    def test_raises_unknown_module(self):
        self.assertRaises(NonExistentModuleError, factorize, module='unknown', object_type='UnknownClass')

    def test_object_creation(self):
        f = factorize(module='factory', object_type='NonExistentModuleError')
        manual = NonExistentModuleError('factory')
        self.assertEqual(type(f), type(manual))

    def test_type_exception(self):
        f = factorize(module='factory', object_type='NonExistentTypeError')
        manual = NonExistentTypeError('NonExistentTypeError')
        self.assertEqual(type(f), type(manual))

if __name__ == '__main__':
    unittest.main()
