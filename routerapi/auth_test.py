#!/usr/bin/python
import unittest
import tempfile
import auth

class TestAuth(unittest.TestCase):
  def setUp(self):
    self.path = tempfile.mkdtemp()
    self.auth = auth.Auth(self.path)

  def test_equal(self):
    self.assertTrue(auth.constant_time_equals("alpha", "alpha"))

  def test_length_differs(self):
    self.assertFalse(auth.constant_time_equals("alpha", "alph"))

  def test_inequal(self):
    self.assertFalse(auth.constant_time_equals("alpha", "beta"))



if __name__ == '__main__':
  unittest.main()
