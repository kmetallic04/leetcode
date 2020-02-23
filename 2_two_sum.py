'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
import unittest

def two_sum(arr, target):
  hash_table = dict()
  for index in range(len(arr)):
    if hash_table.get(target - arr[index]) is not None:
      return (hash_table[target - arr[index]], index)
    hash_table[arr[index]] = index
  return (-1, -1)

class Tests(unittest.TestCase):
  def test_two_sum(self):
    self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))
    
if __name__ == '__main__':
  unittest.main()
