'''
Given a string, find the length of the longest substring without repeating characters.
'''

import unittest

def longest_substring(string):
  seen = dict()
  count = max_count = 0
  
  for index in range(len(string)):
    if seen.get(string[index]):
      seen = dict()
      seen[string[index]] = True
      max_count = max(count, max_count)
      count = 1
    else:
      seen[string[index]] = True
      count += 1
      
  return max_count
  
class Tests(unittest.TestCase):
  def test_longest_substring(self):
    self.assertEqual(longest_substring('abcabcbb'), 3)
    
if __name__ == '__main__':
  unittest.main()
