from collections import Counter
from bisect import insort
from typing import List
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = reduce((lambda x, y: x * y), nums)
        return [s // e for e in nums]

nums= [1,2,3,4]        
print(Solution().productExceptSelf(nums))