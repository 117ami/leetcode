from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=920 lang=python3
#
# [920] Number of Music Playlists
#
# https://leetcode.com/problems/number-of-music-playlists/description/
#
# algorithms
# Hard (45.12%)
# Total Accepted:    7.8K
# Total Submissions: 17.2K
# Testcase Example:  '3\n3\n1'
#
# Your music player contains N different songs and she wants to listen to L
# (not necessarily different) songs during your trip.  You create a playlist so
# that:
#
#
# Every song is played at least once
# A song can only be played again only if K other songs have been played
#
#
# Return the number of possible playlists.  As the answer can be very large,
# return it modulo 10^9 + 7.
#
#
#
#
#
#
# Example 1:
#
#
# Input: N = 3, L = 3, K = 1
# Output: 6
# Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3],
# [2, 3, 1], [3, 1, 2], [3, 2, 1].
#
#
#
# Example 2:
#
#
# Input: N = 2, L = 3, K = 0
# Output: 6
# Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1],
# [2, 2, 1], [2, 1, 2], [1, 2, 2]
#
#
#
# Example 3:
#
#
# Input: N = 2, L = 3, K = 1
# Output: 2
# Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]
#
#
#
#
#
#
# Note:
#
#
# 0 <= K < N <= L <= 100
#
#
#
#
#


class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [[0] * (N + 1) for _ in range(L + 1)]
        dp[0][0] = 1
        mod = pow(10, 9) + 7
        for i in range(1, L + 1):
            for j in range(1, N + 1):
                dp[i][j] = dp[i - 1][j - 1] * (N - j + 1) % mod
                if j > K:
                    dp[i][j] += dp[i - 1][j] * (j - K)
                    dp[i][j] = dp[i][j] % mod
        return dp[L][N]


sol = Solution()
N, L, K = 3, 3, 1
N, L, K = 2, 3, 0
print(sol.numMusicPlaylists(N, L, K))
