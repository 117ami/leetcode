#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#
# https://leetcode.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (40.63%)
# Total Accepted:    13.2K
# Total Submissions: 32.6K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# Given a set of N people (numbered 1, 2, ..., N), we would like to split
# everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the
# same group. 
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the
# people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups
# in this way.
#
#
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
#
#
#
# Example 2:
#
#
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
#
#
#
# Example 3:
#
#
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
#
#
#
# Note:
#
#
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].
#
#
#
#
#
#
import collections


class Solution:
    def find(self, i):
        while i != self.parents[i]:
            i = self.parents[i]
        self.parents[i] = i
        return i

    def possibleBipartition(self, N, dislikes):
        self.parents = [i for i in range(N + 1)]
        m = collections.defaultdict(list)
        for a, b in dislikes:
            m[a].append(b)
            m[b].append(a)

        for i in range(1, N + 1):
            if i in m:
                p1 = self.find(i)
                p2 = self.find(m[i][0])
                if p1 == p2:
                    return False

                for j in m[i][1:]:
                    pj = self.find(j)
                    if pj == p1:
                        return False
                    self.parents[j] = p2
        return True


s = Solution()
N = 5
dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
N, dislikes = 4, [[1, 2], [1, 3], [2, 4]]
print(s.possibleBipartition(N, dislikes))
