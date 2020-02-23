'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

'''

import unittest
import sys

def jump_game(arr, index = 0, memo={}):
  if index >= len(arr):
    return sys.maxsize
  elif index == len(arr) - 1:
    return 0
  else:
    if not memo.get(index):
      minimum = sys.maxsize
      for i in range(1, arr[index] + 1):
        steps = jump_game(arr, index + i, memo) + 1
        if steps < minimum:
          minimum = steps
      memo[index] = minimum
      
    return memo[index]
    
print(jump_game([2,3,1,1,4]))
