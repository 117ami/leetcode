from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
true = True
false = False
#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
#
# algorithms
# Hard (50.08%)
# Total Accepted:    30.6K
# Total Submissions: 61.1K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in ascending order. Find the smallest
# range that includes at least one number from each of the k lists.
#
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c
# if b-a == d-c.
#
#
#
# Example 1:
#
#
# Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
#
#
#
#
# Note:
#
#
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -10^5 <= value of elements <= 10^5.
#
#
#


class Solution:
    def smallestRange(self, ns):
        vv = []
        for i, n in enumerate(ns):
            for j in n:
                vv.append([i, j])
        vv.sort(key=lambda e: e[1])

        k, i, nmax, all_list_seen = len(ns), 0, 1 << 32, False
        memo = {}
        for j, pair in enumerate(vv):
            arrid, v = pair

            if arrid in memo:
                prej = memo[arrid]
                vv[prej][0] = -1
            memo[arrid] = j

            while i < j and vv[i][0] == -1:
                i += 1

            if not all_list_seen:
                all_list_seen = len(memo) == k

            if all_list_seen and v - vv[i][1] < nmax:
                nmax = v - vv[i][1]
                res = [vv[i][1], v]
            # print(memo, i, pair, res)

        return res


s = Solution()
ns = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
print(s.smallestRange(ns))
