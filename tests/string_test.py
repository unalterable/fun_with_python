import sys
sys.path.append('../')
from strings import StringManipulation


import unittest

class StringTests(unittest.TestCase):

  def test_interpolation(self):
    string = StringManipulation().append1('string1', 'string2')
    self.assertTrue(string, 'string1string2')

if __name__ == '__main__':
  unittest.main();

