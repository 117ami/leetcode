#
# @lc app=leetcode id=967 lang=python
#
# [967] Numbers With Same Consecutive Differences
#
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
#
# algorithms
# Medium (29.98%)
# Total Accepted:    2.9K
# Total Submissions: 8.9K
# Testcase Example:  '3\n7'
#
# Return all non-negative integers of length N such that the absolute
# difference between every two consecutive digits is K.
#
# Note that every number in the answer must not have leading zeros except for
# the number 0 itself. For example, 01 has one leading zero and is invalid, but
# 0 is valid.
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
#
# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading
# zeroes.
#
#
#
# Example 2:
#
#
# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
#
#
#
# Note:
#
#
# 1 <= N <= 9
# 0 <= K <= 9
#
#
#


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return list(range(10))
        res = list(range(1, 10))

        for _ in range(1, N):
            tmp = []
            for n in res:
                last_digit = n % 10
                for i in {last_digit - K, last_digit + K}:
                    if i >= 0 and i <= 9:
                        tmp.append(n * 10 + i)
            res = tmp
        return res


print(Solution().numsSameConsecDiff(2, 1))
