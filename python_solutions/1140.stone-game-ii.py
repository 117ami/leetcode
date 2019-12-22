#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#
# https://leetcode.com/problems/stone-game-ii/description/
#
# algorithms
# Medium (60.14%)
# Total Accepted:    6.3K
# Total Submissions: 10.5K
# Testcase Example:  '[2,7,9,4,4]'
#
# Alex and Lee continue their games with piles of stones.  There are a number
# of piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].  The objective of the game is to end with the most stones. 
#
# Alex and Lee take turns, with Alex starting first.  Initially, M = 1.
#
# On each player's turn, that player can take all the stones in the first X
# remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
#
# The game continues until all the stones have been taken.
#
# Assuming Alex and Lee play optimally, return the maximum number of stones
# Alex can get.
#
#
# Example 1:
#
#
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles,
# then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If
# Alex takes two piles at the beginning, then Lee can take all three piles
# left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since
# it's larger.
#
#
#
# Constraints:
#
#
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10 ^ 4
#
#


class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        vsum = [0] * n
        vsum[-1] = piles[-1]

        for i in range(n - 2, -1, -1):
            vsum[i] = vsum[i + 1] + piles[i]
        # print(vsum)
        memo = {}

        from functools import lru_cache
        @lru_cache(None)
        def brute(i, k):
            if (i, k) in memo:
                return memo[(i, k)]
            if i + k * 2 >= n:
                return vsum[i]
            else:
                ans = 0
                for l in range(1, 2 * k + 1):
                    k_next = max(l, k)
                    ans = max(ans, vsum[i] - brute(i + l, k_next))
            memo[(i, k)] = ans
            return ans
        
        res = brute(0, 1) 
        # print(memo)
        return res 
        


s = Solution()
piles = [2, 7, 9, 4, 4] * 20
piles = [9, 2, 2, 8, 3, 7, 9, 9]
piles = [8,9,5,4,5,4,1,1,9,3,1,10,5,9,6,2,7,6,6,9]
# print(piles)
print(s.stoneGameII(piles))
