# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares
# Hard (Difficulty)

# Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.
#  
# Example 1:
#
# Example 2:
#
# Example 3:
#
#  
# Constraints:
# Input: n = 2, m = 3
# Output: 3
# Explanation: 3 squares are necessary to cover the rectangle.
# 2 (squares of 1x1)
# 1 (square of 2x2)
# Input: n = 5, m = 8
# Output: 5
#
# Input: n = 11, m = 13
# Output: 6
#
# xxxxxxxxxx
# class Solution {
# public:
#     int tilingRectangle(int n, int m) {
#         
#     }
# };
import bisect
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def tilingRectangle(self, m, n):
        if m == n:
            return 1
        self.ans = m * n

        def dfs(skylines, steps):
            if all(s == n for s in skylines) or steps >= self.ans:
                self.ans = min(self.ans, steps)
                return

            min_h = min(skylines)
            idx = skylines.index(min_h)
            ridx = idx
            while ridx < m and skylines[ridx] == min_h:
                ridx += 1

            for i in range(min(ridx - idx, n - min_h), 0, -1):
                tmp = skylines[:]
                for j in range(i):
                    tmp[idx + j] += i
                dfs(tmp, steps + 1)

        dfs([0] * m, 0)
        return self.ans


n, m = 11, 13
print(Solution().tilingRectangle(n, m))
