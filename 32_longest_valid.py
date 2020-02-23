'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''

import unittest

def longest_valid(string):
  stack = list()
  max_count = count = 0
  
  for index in range(len(string)):
    if string[index] == '(':
      stack.append('(')
    elif len(stack):
      stack.pop()
      count += 2
      max_count = max(max_count, count)
    else:
      count = 0
      
  return max_count
  
print(longest_valid('())((())'))
