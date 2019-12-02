# https://leetcode.com/problems/number-of-ships-in-a-rectangle
# Hard (Difficulty)

# (This problem is an interactive problem.)
# On the sea represented by a cartesian plane, each ship is located at an integer point, and each integer point may contain at most 1 ship.
# You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true if and only if there is at least one ship in the rectangle represented by the two points, including on the boundary.
# Given two points, which are the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle.  It is guaranteed that there are at most 10 ships in that rectangle.
# Submissions making more than 400 calls to hasShips will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.
#  
# Example :
# 
#  
# Constraints:
# Input: 
# ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
# Output: 3
# Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
# 
# xxxxxxxxxx
# /**
#  * // This is Sea's API interface.
#  * // You should not implement it, or speculate about its implementation
#  * class Sea {
#  *   public:
#  *     bool hasShips(vector<int> topRight, vector<int> bottomLeft);
#  * };
#  */
# ​
# class Solution {
# public:
#     int countShips(Sea sea, vector<int> topRight, vector<int> bottomLeft) {
#         
#     }
# };


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if not sea.hasShips(topRight, bottomLeft): return 0
        x1, y1 = bottomLeft.x, bottomLeft.y 
        x2, y2 = topRight.x, topRight.y 

        ans = 0
        if y2 - y1 <= 2 and x2 - x1 <= 2:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    p = Point(i, j)
                    ans += 1 if sea.hasShips(p, p) else 0
            return ans
        else:
            if y2 - y1 > x2 - x1:
                y3 = (y2 + y1) // 2 
                return self.countShips(sea, topRight, Point(x1, y3 + 1)) + self.countShips(sea, Point(x2, y3), bottomLeft)
            else:
                x3 = (x1 + x2) // 2
                return self.countShips(sea, topRight, Point(x3 + 1, y1)) + self.countShips(sea, Point(x3, y2), bottomLeft)
                        
            
