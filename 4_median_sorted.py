'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''

import unittest

def median_sorted(nums1, nums2):
  min_index = 0
  max_index = len(nums1)
  
  while min_index <= max_index:
    i = int((min_index + max_index) / 2)
    j = int((len(nums1) + len(nums2) + 1) / 2) - i
    
    if i < len(nums1) and j > 0 and nums2[j - 1] > nums1[i]:
      min_index = i + 1
    elif i > 0 and j < len(nums2) and nums1[i - 1] > nums2[j]:
      max_index = i - 1
    else:
      if i == 0:
        median = nums2[j - 1]
      elif j == 0:
        median = nums1[i - 1]
      else:
        median = max(nums2[j - 1], nums1[i - 1])
      break
        
  if (len(nums1) + len(nums2)) % 2:
    return median
  
  if i == len(nums1):
    return (median + nums2[j]) / 2.0
    
  if j == len(nums2):
    return (median + nums1[j]) / 2.0
    
  return (median + min(nums1[i], nums2[j])) / 2.0
    
print(median_sorted([1,9],[1,2,3,4,5,6,7,8,9]))
