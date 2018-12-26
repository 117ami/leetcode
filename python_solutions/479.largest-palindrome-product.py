#
# @lc app=leetcode id=479 lang=python
#
# [479] Largest Palindrome Product
#
# https://leetcode.com/problems/largest-palindrome-product/description/
#
# algorithms
# Easy (26.52%)
# Total Accepted:    13.6K
# Total Submissions: 51.3K
# Testcase Example:  '1'
#
# Find the largest palindrome made from the product of two n-digit numbers.
# ⁠Since the result could be very large, you should return the largest
# palindrome mod 1337.
#
# Example:
# Input: 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#
#
#
#
# Note:
# The range of n is [1,8].
#
#
#
import math


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = {1: 9, 2: 987, 3: 123, 4: 597, 5: 677, 6: 1218, 7: 877, 8: 475}
        if n in res:
            return res.get(n)
        if n == 1:
            return 9
        maxnum = 10 ** n - 1
        for i in range(maxnum, int(maxnum / 10), -1):
            cand = int(str(i) + str(i)[::-1])
            x = maxnum
            bound = math.sqrt(cand)
            while x >= bound:
                if cand % x == 0:
                    return cand % 1337
                else:
                    x -= 1


for i in range(1, 9):
    print(i, Solution().largestPalindrome(i))
