import collections
#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (47.89%)
# Total Accepted:    48.2K
# Total Submissions: 100.6K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them.
#
# Two trees are duplicate if they have the same structure with same node
# values.
#
# Example 1:
#
#
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
#
#
# The following are two duplicate subtrees:
#
#
# ⁠     2
# ⁠    /
# ⁠   4
#
#
# and
#
#
# ⁠   4
#
# Therefore, you need to return above trees' root in the form of a list.
#
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def tree_from_list(arr):
    if not arr:
        return
    children = 0
    i = 1
    jobs = [TreeNode(arr[0])]
    root = jobs[0]
    while i < len(arr):
        if children == 2:
            jobs.pop(0)
            children = 0

        if arr[i]:
            c = TreeNode(arr[i])
            if children == 0:
                jobs[0].left = c
            else:
                jobs[0].right = c
            jobs.append(c)

        children += 1
        i += 1

    return root


class Solution:
    def getdepth(self, r):
        if not r:
            return 0
        return 1 + max(self.getdepth(r.left), self.getdepth(r.right))

    def printTree(self, root):
        self.d = self.getdepth(root)
        width = 2**self.d - 1
        res = [[""] * width for _ in range(self.d)]

        def dfs(node, depth, loc):
            if not node or depth > self.d:
                return
            res[depth - 1][loc] = str(node.val)
            offset = 2 ** (self.d - depth - 1)
            dfs(node.left, depth + 1, loc - offset)
            dfs(node.right, depth + 1, loc + offset)

        dfs(root, 1, width // 2)
        for layer in res:
            print(layer)
        return res

    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        count = collections.Counter()
        ans = []
        trees.default_factory = trees.__len__

        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        print(trees)
        return ans


s = Solution()
arr = [1, 2, 3, 4, None, 2, 4, None, None, 4]
root = tree_from_list(arr)
print(s.findDuplicateSubtrees(root))
