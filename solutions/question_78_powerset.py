from itertools import combinations
"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        for i in range(len(nums) + 1):
            for e in list(combinations(nums, i)):
                r.append(list(e))
        return r


Solution().subsets([1, 2, 3])
