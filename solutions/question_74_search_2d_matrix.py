# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                break
            i += 1
        if target in matrix[i - 1]:
            return True
        else:
            return False


m = [[1, 3, 5, 7],
     [10, 11, 16, 20],
     [23, 30, 34, 50]]

r = Solution().searchMatrix(m, 29)
print(r)
