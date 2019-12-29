from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=1300 lang=python3
#
# [1300] Sum of Mutated Array Closest to Target
#
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/description/
#
# algorithms
# Medium (41.26%)
# Total Accepted:    1.6K
# Total Submissions: 3.9K
# Testcase Example:  '[4,9,3]\n10'
#
# Given an integer array arr and a target value target, return the integer
# value such that when we change all the integers larger than value in the
# given array to be equal to value, the sum of the array gets as close as
# possible (in absolute difference) to target.
#
# In case of a tie, return the minimum such integer.
#
# Notice that the answer is not neccesarilly a number from arr.
#
#
# Example 1:
#
#
# Input: arr = [4,9,3], target = 10
# Output: 3
# Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's
# the optimal answer.
#
#
# Example 2:
#
#
# Input: arr = [2,3,5], target = 10
# Output: 5
#
#
# Example 3:
#
#
# Input: arr = [60864,25176,27249,21296,20204], target = 56803
# Output: 11361
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^4
# 1 <= arr[i], target <= 10^5
#
#


class Solution:
    def findBestValue(self, arr, target):
        lo, hi = 0, target
        while lo < hi:
            mid = (lo + hi) / 2
            cur = sum(n if n <= mid else mid for n in arr)
            if cur < target:
                lo = mid + 0.5
            elif cur > target:
                hi = mid - 0.5
            else:
                return int(round(mid))
        diff = lambda n: abs(target - sum(i if i <= n else n for i in arr))
        res = int(lo)
        # print(res, diff(res), diff(res+1))
        return res if diff(res) <= diff(res + 1) else res + 1


sol = Solution()
arr, target = [4, 9, 3], 10
arr, target = [2,3,5], 10
arr, target = [60864, 25176, 27249, 21296, 20204], 56803
arr, target = [1547,83230,57084,93444,70879], 71237
print(sol.findBestValue(arr, target))
