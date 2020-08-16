from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007


#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (43.27%)
# Total Accepted:    22.5K
# Total Submissions: 52K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
#
#
#
# Example 1:
#
#
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation:
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
#
#
# Note:
#
#
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
#
#
class Solution:
    def at_most(self, m, nums):
        if m < 0: return 0
        cnt, i, n = 0, 0, len(nums)
        for j in range(n):
            m -= nums[j]
            while m < 0:
                m += nums[i]
                i += 1
            cnt += j - i + 1
        return cnt

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        return self.at_most(S, A) - self.at_most(S - 1, A)


sol = Solution()
A, S = [1, 0, 1, 0, 1], 2
print(sol.numSubarraysWithSum(A, S))
