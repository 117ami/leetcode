#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#
# https://leetcode.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (50.35%)
# Total Accepted:    8.7K
# Total Submissions: 17.3K
# Testcase Example:  '1'
#
# Starting with a positive integer N, we reorder the digits in any order
# (including the original order) such that the leading digit is not zero.
#
# Return true if and only if we can do this in a way such that the resulting
# number is a power of 2.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: 1
# Output: true
#
#
#
# Example 2:
#
#
# Input: 10
# Output: false
#
#
#
# Example 3:
#
#
# Input: 16
# Output: true
#
#
#
# Example 4:
#
#
# Input: 24
# Output: false
#
#
#
# Example 5:
#
#
# Input: 46
# Output: true
#
#
#
#
# Note:
#
#
# 1 <= N <= 10^9
#
#
#
#
#
#
#
#


class Solution:
    def reorderedPowerOf2(self, n):
        arr = sorted(list(str(n)))
        bound = int(''.join(reversed(arr)))
        i = 1
        while i <= bound:
            if sorted(list(str(i))) == arr:
                return True
            i *= 2
        return False


print(Solution().reorderedPowerOf2(4021))
