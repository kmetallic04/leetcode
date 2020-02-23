'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

import unittest

def generate_parentheses(n):
  opening, closing, list = ['('] * n, [')'] * n, []
  generate_parentheses_helper(opening, closing, [], list)
  return list

def generate_parentheses_helper(opening, closing, current, list):
  if len(opening) == 0:
    list.append(''.join(current + closing))
  else:
    if len(opening) < len(closing):
      current.append(closing.pop())
      generate_parentheses_helper(opening, closing, current, list)
      closing.append(current.pop())
      
    current.append(opening.pop())
    generate_parentheses_helper(opening, closing, current, list)
    opening.append(current.pop())
    
class Tests(unittest.TestCase):
  def test_generate_parentheses(self):
    self.assertEqual(generate_parentheses(3), ['()()()', '()(())', '(())()', '(()())', '((()))'])
    self.assertEqual(generate_parentheses(2), ['()()', '(())'])
    
if __name__ == '__main__':
  unittest.main()
