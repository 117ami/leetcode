from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1361 lang=python3
#
# [1361] Validate Binary Tree Nodes
#
# https://leetcode.com/problems/validate-binary-tree-nodes/description/
#
# algorithms
# Medium (69.16%)
# Total Accepted:    4.7K
# Total Submissions: 6.7K
# Testcase Example:  '4\n[1,-1,3,-1]\n[2,-1,-1,-1]'
#
# You have n binary tree nodes numbered from 0 to n - 1 where node i has two
# children leftChild[i] and rightChild[i], return true if and only if all the
# given nodes form exactly one valid binary tree.
# 
# If node i has no left child then leftChild[i] will equal -1, similarly for
# the right child.
# 
# Note that the nodes have no values and that we only use the node numbers in
# this problem.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false
# 
# 
# Example 4:
# 
# 
# 
# 
# Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# leftChild.length == rightChild.length == n
# -1 <= leftChild[i], rightChild[i] <= n - 1
# 
# 
#
class Solution:
    def validateBinaryTreeNodes(self, n: int, lc, rc):
        seen = set()
        children = {}
        for i, l in enumerate(lc):
            children[i] = (l, rc[i])
        st = [0]
        while st:
            cur = st.pop()
            if cur in seen: return false 
            seen.add(cur)
            x, y = children[cur]
            if x >= 0:
                st.append(x)
            if y >= 0:
                st.append(y)
        return len(seen) == n
        
sol = Solution()
n, lc, rc = 4, [1,-1,3,-1], [2,-1,-1,-1]
n, lc, rc = 4, [1,-1,3,-1], [2,3,-1,-1]
n, lc, rc = 2, [1,0], [-1,-1]
n, lc, rc = 6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1]
print(sol.validateBinaryTreeNodes(n, lc, rc))


