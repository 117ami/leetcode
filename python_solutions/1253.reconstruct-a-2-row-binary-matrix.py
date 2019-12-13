#
# @lc app=leetcode id=1253 lang=python3
#
# [1253] Reconstruct a 2-Row Binary Matrix
#
# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/description/
#
# algorithms
# Medium (38.37%)
# Total Accepted:    6.5K
# Total Submissions: 17K
# Testcase Example:  '2\n1\n[1,1,1]'
#
# Given the following details of a matrix with n columns and 2 rows :
#
#
# The matrix is a binary matrix, which means each element in the matrix can be
# 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum
# is given as an integer array with length n.
#
#
# Your task is to reconstruct the matrix with upper, lower and colsum.
#
# Return it as a 2-D integer array.
#
# If there are more than one valid solution, any of them will be accepted.
#
# If no valid solution exists, return an empty 2-D array.
#
#
# Example 1:
#
#
# Input: upper = 2, lower = 1, colsum = [1,1,1]
# Output: [[1,1,0],[0,0,1]]
# Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct
# answers.
#
#
# Example 2:
#
#
# Input: upper = 2, lower = 3, colsum = [2,2,1,1]
# Output: []
#
#
# Example 3:
#
#
# Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
#
#
#
# Constraints:
#
#
# 1 <= colsum.length <= 10^5
# 0 <= upper, lower <= colsum.length
# 0 <= colsum[i] <= 2
#
#
#


class Solution:
    def reconstructMatrix(self, upper, lower, cs):
        n = len(cs)
        res = [[0] * n, [0] * n]
        for i in range(n):
            if cs[i] == 2:
                res[0][i] = res[1][i] = 1
                upper -= 1
                lower -= 1

        if upper < 0 or lower < 0:
            return []
        for i in range(n):
            if cs[i] == 1:
                if upper > 0:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
        return res if lower == 0 else []


s = Solution()
upper, lower, cs = 5, 5, [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]
upper, lower, cs = 1, 4, [2, 1, 2, 0, 0, 2]
# upper, lower, cs = 9, 2, [0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2]
# upper, lower, cs = 2, 1, [1, 1, 1]
# print(cs.count(2))
res = s.reconstructMatrix(upper, lower, cs)
print(res)
# print(res[0], res[1], sep="\n")
