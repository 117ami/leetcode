#
# @lc app=leetcode id=891 lang=python
#
# [891] Sum of Subsequence Widths
#
# https://leetcode.com/problems/sum-of-subsequence-widths/description/
#
# algorithms
# Hard (26.58%)
# Total Accepted:    3.4K
# Total Submissions: 12.9K
# Testcase Example:  '[2,1,3]'
#
# Given an array of integers A, consider all non-empty subsequences of A.
#
# For any sequence S, let the width of S be the difference between the maximum
# and minimum element of S.
#
# Return the sum of the widths of all subsequences of A. 
#
# As the answer may be very large, return the answer modulo 10^9 + 7.
#
#
#
#
# Example 1:
#
#
# Input: [2,1,3]
# Output: 6
# Explanation:
# Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
# The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
# The sum of these widths is 6.
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 20000
# 1 <= A[i] <= 20000
#
#
#
#


class Solution(object):
    def sumSubseqWidths2(self, a):
        """ my own solution
        :type A: List[int]
        :rtype: int
        """
        a.sort()
        maxn = minn = 0
        mod = 10 ** 9 + 7
        co = 1
        for n in a:
            maxn = (maxn + co * n) % mod
            co = (co * 2) % mod
            maxn = maxn % mod

        co = 1
        for n in a[::-1]:
            minn = (minn + co * n) % mod
            co = (co * 2) % mod

        return (mod + maxn - minn) % mod

    def sumSubseqWidths(self, a):
        # someone else's solution, quite smart
        a.sort()
        res = 0
        for i, n in enumerate(a):
            res <<= 1
            res += a[~i] - n
            res %= 10 ** 9 + 7
        return res % (10**9 + 7)


a = [2, 1, 3]
print(Solution().sumSubseqWidths(a))
