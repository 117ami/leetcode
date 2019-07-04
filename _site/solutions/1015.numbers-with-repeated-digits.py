#
# @lc app=leetcode id=1015 lang=python3
#
# [1015] Numbers With Repeated Digits
#
# https://leetcode.com/problems/numbers-with-repeated-digits/description/
#
# algorithms
# Hard (33.80%)
# Total Accepted:    1.8K
# Total Submissions: 5.3K
# Testcase Example:  '20'
#
# Given a positive integer N, return the number of positive integers less than
# or equal to N that have at least 1 repeated digit.
#
#
#
#
# Example 1:
#
#
# Input: 20
# Output: 1
# Explanation: The only positive number (<= 20) with at least 1 repeated digit
# is 11.
#
#
#
# Example 2:
#
#
# Input: 100
# Output: 10
# Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are
# 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
#
#
#
# Example 3:
#
#
# Input: 1000
# Output: 262
#
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


class Solution:
    def numDupDigitsAtMostN(self, N):
        D = list(map(int, str(N + 1)))
        n = len(D)

        def per(m, n):
            return 1 if n == 0 else per(m, n - 1) * (m - n + 1)

        res = sum([9 * per(9, i) for i in range(n - 1)])
        s = set()
        for i, x in enumerate(D):
            for y in range(0 if i else 1, x):
                if y not in s:
                    res += per(9 - i, n - i - 1)
            if x in s:
                break
            s.add(x)
        return N - res


N = 1000
print(Solution().numDupDigitsAtMostN(N))
