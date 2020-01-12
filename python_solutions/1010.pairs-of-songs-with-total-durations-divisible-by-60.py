from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Easy (46.73%)
# Total Accepted:    23.4K
# Total Submissions: 50K
# Testcase Example:  '[30,20,150,100,40]'
#
# In a list of songs, the i-th song has a duration of time[i] seconds. 
# 
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60.  Formally, we want the number of indices i < j with
# (time[i] + time[j]) % 60 == 0.
# 
# 
# 
# Example 1:
# 
# 
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# 
# 
# 
# Example 2:
# 
# 
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible
# by 60.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500
# 
#
class Solution:
    def numPairsDivisibleBy60(self, time):
        res = 0
        cc = defaultdict(int)
        for t in time:
            x = t % 60
            y = (60 - x) % 60
            if y in cc:
                res += cc[y]
            cc[x] += 1
        return res 

sol = Solution()
time = [30,20,150,100,40]
time = [60, 60, 60]
print(sol.numPairsDivisibleBy60(time))

