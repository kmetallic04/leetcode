'''
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''

import unittest

def roman_to_integer(string):
  romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
  
  digit = romans[string[len(string) - 1]]
  
  for index in range(len(string) - 2, -1, -1):
    if romans[string[index]] < romans[string[index + 1]]:
      digit -= romans[string[index]]
    else:
      digit += romans[string[index]]
      
  return digit
  
class Tests(unittest.TestCase):
  def test_roman_to_integer(self):
    self.assertEqual(roman_to_integer('LVIII'), 58)
    self.assertEqual(roman_to_integer('MCMXCIV'), 1994)
    
if __name__ == '__main__':
  unittest.main()
