# Example 1: A basic example

# Why do we need unit tests?

import unittest


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.test_str = "FOO"

    def test_upper(self):
        self.assertEqual("foo".upper(), self.test_str)

    def tearDown(self):
        del self.test_str
