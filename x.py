from collections import Counter
from bisect import insort
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = res = 0
        sz = len(nums)
        cache = [float('-inf')] * (sz * 2 + 1)
        cache[sz] = -1

        for i, n in enumerate(nums):
            diff += 1 if n == 1 else -1
            if cache[diff + sz] < -sz:
                cache[diff + sz] = i
            res = max(res, i - cache[diff + sz])

        return res


nums = [1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1]
nums = [0, 1, 0]
nums = []
print(Solution().findMaxLength(nums))
