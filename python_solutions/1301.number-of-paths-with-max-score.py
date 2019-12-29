from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=1301 lang=python3
#
# [1301] Number of Paths with Max Score
#
# https://leetcode.com/problems/number-of-paths-with-max-score/description/
#
# algorithms
# Hard (30.57%)
# Total Accepted:    1.1K
# Total Submissions: 3.4K
# Testcase Example:  '["E23","2X2","12S"]\r'
#
# You are given a square board of characters. You can move on the board
# starting at the bottom right square marked with the character 'S'.
#
# You need to reach the top left square marked with the character 'E'. The rest
# of the squares are labeled either with a numeric character 1, 2, ..., 9 or
# with an obstacle 'X'. In one move you can go up, left or up-left (diagonally)
# only if there is no obstacle there.
#
# Return a list of two integers: the first integer is the maximum sum of
# numeric characters you can collect, and the second is the number of such
# paths that you can take to get that maximum sum, taken modulo 10^9 + 7.
#
# In case there is no path, return [0, 0].
#
#
# Example 1:
# Input: board = ["E23","2X2","12S"]
# Output: [7,1]
# Example 2:
# Input: board = ["E12","1X1","21S"]
# Output: [4,2]
# Example 3:
# Input: board = ["E11","XXX","11S"]
# Output: [0,0]
#
#
# Constraints:
#
#
# 2 <= board.length == board[i].length <= 100
#
#


class Solution:
    def pathsWithMaxScore(self, board):
        n = len(board)
        dp = [[(0, 0)] * n for _ in range(n)]
        board[-1] = board[-1][:-1] + "0"
        # for i in range(n):
        #     dp[1][i] = board[0]
        MIN = -0x3f3f3f3f
        mod = pow(10, 9)+7
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    dp[i][j] = (MIN, 1)
                elif i == 0 and j == 0:
                    dp[i][j] = (0, 1)
                elif i == 0:
                    dp[i][j] = (int(board[i][j]) + dp[i][j - 1][0], 1)
                elif j == 0:
                    dp[i][j] = (int(board[i][j]) + dp[i - 1][j][0], 1)
                else:
                    # print(i , j)
                    value, count = dp[i][j]
                    value = int(board[i][j])
                    vmax = max(t[0] for t in  [dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]])
                    for ivalue, icount in [dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]]:
                        if ivalue == vmax:
                            count += icount
                    value += vmax 
                    count %= mod 
                    dp[i][j] = (value, count)
                # if dp[i][j] == 27:
                #     print(i, j)
        
        # for i in dp:
            # print(i)
        value, count = dp[-1][-1]
        return [value, count] if value >= 0 else [0, 0]


sol = Solution()
board = ["E23", "2X2", "12S"]
# board = ["E12", "1X1", "21S"]
# board = ["EX", "XS"]
board = ["E11345","X452XX","3X43X4","44X312","23452X","1342XS"]
# board = ["E11","XXX","11S"]
print(sol.pathsWithMaxScore(board))
