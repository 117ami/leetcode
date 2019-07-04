#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (47.74%)
# Total Accepted:    23.6K
# Total Submissions: 49.5K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# We are given a binary tree (with root node root), a target node, and an
# integer value K.
#
# Return a list of the values of all nodes that have a distance K from the
# target node.  The answer can be returned in any order.
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
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
#
# Output: [7,4,1]
#
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
#
#
#
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these
# objects.
#
#
#
#
# Note:
#
#
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
#
#
#
#
# Definition for a binary tree node.
# import aux


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root, target, K):
        root.parent = None
        self.set_parent(root)
        layer = [target]
        visited = set(layer)
        for _ in range(K):
            layer = [x for n in layer for x in (n.left, n.right, n.parent) if x and x not in visited]
            visited.update(layer)

        return [n.val for n in layer]


    def set_parent(self, r):
        if r.left:
            r.left.parent = r
            self.set_parent(r.left)
        if r.right:
            r.right.parent = r
            self.set_parent(r.right)

    def distanceK2(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.m = {}
        self.res = []
        self.find(root, target)
        self.dfs(root, target, self.m[root], K)
        return self.res

    def find(self, r, target):
        if r is None:
            return -1
        if r.val == target.val:
            self.m[r] = 0
            return 0
        left = self.find(r.left, target)
        if left >= 0:
            self.m[r] = left + 1
            return left + 1
        right = self.find(r.right, target)
        if right >= 0:
            self.m[r] = right + 1
            return right + 1
        return -1

    def dfs(self, r, target, l, K):
        if r is None:
            return
        if r in self.m:
            l = self.m[r]
        if l == K:
            self.res.append(r.val)
        self.dfs(r.left, target, l + 1, K)
        self.dfs(r.right, target, l + 1, K)


# s = Solution()
# root = aux.tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
# print(root.right.right.val)
# print(s.distanceK(root, TreeNode(5), 2))
