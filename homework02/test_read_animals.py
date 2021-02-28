#!/usr/bin/env python3
import unittest
from read_animals import breed

class TestReadAnimals(unittest.TestCase):

    def test_breeding(self):
        self.assertRaises(TypeError, breed, 1)
        self.assertRaises(TypeError, breed, True)

if __name__=='__main__':
    unittest.main()
