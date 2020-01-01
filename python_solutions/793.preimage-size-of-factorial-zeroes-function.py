from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=793 lang=python3
#
# [793] Preimage Size of Factorial Zeroes Function
#
# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/description/
#
# algorithms
# Hard (39.64%)
# Total Accepted:    6.8K
# Total Submissions: 17.1K
# Testcase Example:  '0'
#
# Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 *
# 3 * ... * x, and by convention, 0! = 1.)
#
# For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) =
# 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many
# non-negative integers x have the property that f(x) = K.
#
#
# Example 1:
# Input: K = 0
# Output: 5
# Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.
#
# Example 2:
# Input: K = 5
# Output: 0
# Explanation: There is no x such that x! ends in K = 5 zeroes.
#
#
# Note:
#
#
# K will be an integer in the range [0, 10^9].
#
#
#


class Solution:
    def preimageSizeFZF(self, k):
        def count(n):
            if n == 0:
                return 0
            return count(n // 5) + n // 5
        lo, hi = 0, 5 * k + 1

        while lo < hi:
            mid = (lo + hi) // 2
            cc = count(mid)
            if cc < k:
                lo = mid + 1
            elif cc > k:
                hi = mid - 1
            else:
                return 5
        return 0


sol = Solution()
print(sol.preimageSizeFZF(5))
