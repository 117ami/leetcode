#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (72.62%)
# Total Accepted:    40.4K
# Total Submissions: 55.7K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
# 
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
# 
# 
# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Note:
# 
# 
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of
# nodes inside one path.
# 
#
class Solution:
    def allPathsSourceTarget(self, graph):
        self.n = len(graph)
        def dfs(i):
            if i == self.n - 1: return [[self.n - 1]]
            if len(graph[i]) == 0:
                return [[]]

            res = []
            for j in graph[i]:
                for path in dfs(j):
                    if len(path) > 0:
                        res.append([i] + path)
            # print(i, path)
            return res     
        return dfs(0)

s = Solution()
graph = [[1,2], [3], [3], []] 
print(s.allPathsSourceTarget(graph))

