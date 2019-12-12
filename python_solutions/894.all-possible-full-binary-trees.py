#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#
# https://leetcode.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (72.57%)
# Total Accepted:    26.2K
# Total Submissions: 36.1K
# Testcase Example:  '7'
#
# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
# 
# Return a list of all possible full binary trees with N nodes.  Each element
# of the answer is the root node of one possible tree.
# 
# Each node of each tree in the answer must have node.val = 0.
# 
# You may return the final list of trees in any order.
# 
# 
# 
# Example 1:
# 
# 
# Input: 7
# Output:
# [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 20
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import itertools
class Solution:
    cache = {0:[], 1:[TreeNode(0)]}
    def allPossibleFBT(self, n):
        if n in Solution.cache: return Solution.cache[n]
        res = []
        for i in range(1, n, 2):
            for l, r in itertools.product(self.allPossibleFBT(i), self.allPossibleFBT(n - i - 1)):
                tmp = TreeNode(0)
                tmp.left = l 
                tmp.right = r
                res.append(tmp)
        
        Solution.cache[n] = res 
        return res


for l, r in itertools.product([2, 3, 4], [8, 2]):
    print(l, r)

        



s = Solution()


