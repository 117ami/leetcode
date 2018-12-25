#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (38.30%)
# Total Accepted:    176.9K
# Total Submissions: 461.9K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        line0 = 1
        for i in range(row):
        	if matrix[i][0] == 0 : line0 = 0
        	for j in range(1, col):
        		if matrix[i][j] == 0:
        			matrix[i][0] = 0
        			matrix[0][j] = 0

        for i in range(row)[::-1]:
        	for j in reversed(range(1, col)):
        		if matrix[i][0] == 0 or matrix[0][j] == 0:
        			matrix[i][j] = 0
        	if line0 == 0: matrix[i][0] = 0

        # print(matrix)

matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

matrix = [
	[1, 1, 1],
	[0, 1, 2]
]
Solution().setZeroes(matrix)