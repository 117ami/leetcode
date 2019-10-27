#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#
# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
#
# algorithms
# Easy (47.46%)
# Total Accepted:    7.7K
# Total Submissions: 16.3K
# Testcase Example:  '[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]'
#
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
# represents the coordinate of a point. Check if these points make a straight
# line in the XY plane.
#
#
#
#
# Example 1:
#
#
#
#
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
#
#
# Example 2:
#
#
#
#
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
#
#
#
# Constraints:
#
#
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.
#
#
#


class Solution:
    def checkStraightLine(self, coordinates):
        x1, y1 = coordinates[0]
        x, y = coordinates[1][0] - x1, coordinates[1][1] - y1
        
        for i, j in coordinates[2:]:
            if x * (j - y1) != y * (i - x1):
                return False 
        return True


s = Solution()
coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
print(s.checkStraightLine(coordinates))
