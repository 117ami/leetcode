# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
from typing import List 

class BinaryMatrix(object):
   def get(self, x: int, y: int) -> int:
       pass 
   def dimensions(self):
       pass 

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()[:2]
        res = m
        for i in range(n):
            low, high = 0, m - 1
            while low < high:
                mid = (low + high) // 2 
                if binaryMatrix.get(i, mid) == 1:
                    high = mid 
                else:
                    low = mid + 1
            if res > low and binaryMatrix.get(i, low) == 1:
                res = low
        return res if res < m else -1
