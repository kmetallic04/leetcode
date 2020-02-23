'''
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
'''

import unittest

def integer_to_roman(digit):
  romans = {
    0: ['I', 'V', 'X'],
    1: ['X', 'L', 'C'],
    2: ['C', 'D', 'M'],
    3: ['M']
  }
  
  power = 0
  output = ''
  
  while digit > 0:
    current = digit % 10
    
    if current < 9:
      if current < 5:
        if current == 4:
          output = romans[power][0] + romans[power][1] + output
        else:
          output = romans[power][0] * current + output
      else:
        output = romans[power][1] + romans[power][0] * (current - 5) + output
    else:
      output = romans[power][0] * (10 - current) + romans[power][2] + output
      
    power += 1
    digit = digit // 10
    
  return output
    
class Tests(unittest.TestCase):
  def test_integer_to_roman(self):
    self.assertEqual(integer_to_roman(58), 'LVIII')
    self.assertEqual(integer_to_roman(1994), 'MCMXCIV')
    
if __name__ == '__main__':
  unittest.main()
