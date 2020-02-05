from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br
from functools import reduce, lru_cache
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/
#
# algorithms
# Hard (53.63%)
# Total Accepted:    3.2K
# Total Submissions: 6K
# Testcase Example:  '[6,5,4,3,2,1]\n2'
#
# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To
# work on the i-th job, you have to finish all the jobs j where 0 <= j < i).
#
# You have to finish at least one task every day. The difficulty of a job
# schedule is the sum of difficulties of each day of the d days. The difficulty
# of a day is the maximum difficulty of a job done in that day.
#
# Given an array of integers jobDifficulty and an integer d. The difficulty of
# the i-th job is jobDifficulty[i].
#
# Return the minimum difficulty of a job schedule. If you cannot find a
# schedule for the jobs return -1.
#
#
# Example 1:
#
#
# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7
#
#
# Example 2:
#
#
# Input: jobDifficulty = [9,9,9], d = 4
# Output: -1
# Explanation: If you finish a job per day you will still have a free day. you
# cannot find a schedule for the given jobs.
#
#
# Example 3:
#
#
# Input: jobDifficulty = [1,1,1], d = 3
# Output: 3
# Explanation: The schedule is one job per day. total difficulty will be 3.
#
#
# Example 4:
#
#
# Input: jobDifficulty = [7,1,7,1,7,1], d = 3
# Output: 15
#
#
# Example 5:
#
#
# Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
# Output: 843
#
#
#
# Constraints:
#
#
# 1 <= jobDifficulty.length <= 300
# 0 <= jobDifficulty[i] <= 1000
# 1 <= d <= 10
#
#


class Solution:
    def minDifficulty(self, jobs, d):

        memo = {}

        @lru_cache(None)
        def dfs(i, d):
            if (i, d) in memo: return memo[(i, d)]
            n = len(jobs)

            if i + d > n: return MAX
            if d == 1: return max(jobs[i:])
            if i + d == n: return sum(jobs[i:])

            pre, res = jobs[i], MAX
            for j in range(i, n):
                pre = max(pre, jobs[j])
                res = min(res, pre + dfs(j+1, d-1))
                # print(i, d, pre, res, j)
            memo[(i, d)] = res
            return res

        r = dfs(0, d)
        return r if r < MAX else -1


sol = Solution()
jobs, d = [11, 111, 22, 222, 33, 333, 44, 444], 6
# jobs, d = [7, 1, 7, 1, 7, 1], 3
# jobs, d = [6,5,4,3,2,1], 2
print(sol.minDifficulty(jobs, d))
