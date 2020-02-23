'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.
'''

import unittest
import math

def divide_two(dividend, divisor):
  sign = 1 if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) else -1
  dividend, divisor = abs(dividend), abs(divisor)
  
  remainder, output = 0, 0
  for shift in range(math.ceil(math.log(dividend) / math.log(divisor)), -1, -1):
    last_bit = 1 if dividend & 1 << shift else 0
    remainder = remainder + remainder + last_bit
    if remainder >= divisor:
      output += 2 ** shift
      remainder -= divisor
      
  return sign * output
  
class Tests(unittest.TestCase):
  def test_divide_two(self):
    self.assertEqual(divide_two(10, 3), 3)
    self.assertEqual(divide_two(105, -3), -35)
    
if __name__ == '__main__':
  unittest.main()
