'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

'''

import unittest

def spiral_matrix_helper(matrix, left, right, top, bottom, list):
  if left == right:
    for index in range(top, bottom + 1):
      list.append(matrix[index][left])
  elif top == bottom:
    for index in range(left, right + 1):
      list.append(matrix[top][index])
  elif left < right and top < bottom:
    for index in range(left, right + 1):
      list.append(matrix[top][index])
    for index in range(top + 1, bottom + 1):
      list.append(matrix[index][right])
    for index in range(right - 1, left - 1, -1):
      list.append(matrix[bottom][index])
    for index in range(bottom - 1, top, -1):
      list.append(matrix[index][left])
      
    spiral_matrix_helper(matrix, left + 1, right - 1, top + 1, bottom - 1, list)
    
def spiral_matrix(matrix):
  list = []
  spiral_matrix_helper(matrix, 0, len(matrix[0]) - 1, 0, len(matrix) - 1, list)
  return list

class Tests(unittest.TestCase):
  def test_spiral_matrix(self):
    matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ] 
    self.assertEqual(spiral_matrix(matrix), [1,2,3,4,8,12,11,10,9,5,6,7])
    matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
    self.assertEqual(spiral_matrix(matrix), [1,2,3,6,9,8,7,4,5])

if __name__ == '__main__':
  unittest.main()
