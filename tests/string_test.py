import sys
sys.path.append('../')
from strings import StringManipulation


import unittest

class StringTests(unittest.TestCase):

  def test_interpolation(self):
    string = StringManipulation().append1('string1', 'string2')
    self.assertEqual(string, 'string1string2')
  
  def test_slice(self):
    string = StringManipulation().slice1('identifier', 4)
    print string
    self.assertEqual(string, 'iden')

if __name__ == '__main__':
  unittest.main();

