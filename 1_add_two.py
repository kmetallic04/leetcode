'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''

import unittest
import linked_list
    
def add_two(linkedList1, linkedList2):
  digit1 = to_digit(linkedList1)
  digit2 = to_digit(linkedList2)
  
  digit = digit1 + digit2
  linkedList = linked_list.LinkedList()
  
  while digit > 0:
    linkedList.addNode(Node(digit - (digit // 10) * 10))
    digit /= 10
    
  return linkedList.listify()
  
def to_digit(linkedList):
  node = linkedList.head
  digit, power = 0, 0
  
  while node is not None:
    digit += node.data * 10 ** power
    power += 1
    
  return digit
  
class Tests(unittest.TestCase):
  def test_add_two(self):
    linkedList1 = linked_list.LinkedList([2,4,3])
    linkedList2 = linked_list.LinkedList([5,6,4])
    self.assertEqual(add_two(linkedList1, linkedList2), [7,0,8])
    
if __name__ == '__main__':
  unittest.main()
