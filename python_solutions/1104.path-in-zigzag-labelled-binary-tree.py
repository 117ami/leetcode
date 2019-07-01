#
# @lc app=leetcode id=1104 lang=python3
#
# [1104] Path In Zigzag Labelled Binary Tree
#
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/description/
#
# algorithms
# Easy (69.58%)
# Total Accepted:    2.6K
# Total Submissions: 3.8K
# Testcase Example:  '14'
#
# In an infinite binary tree where every node has two children, the nodes are
# labelled in row order.
#
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is
# left to right, while in the even numbered rows (second, fourth, sixth,...),
# the labelling is right to left.
#
#
#
# Given the label of a node in this tree, return the labels in the path from
# the root of the tree to the node with that label.
#
#
# Example 1:
#
#
# Input: label = 14
# Output: [1,3,4,14]
#
#
# Example 2:
#
#
# Input: label = 26
# Output: [1,2,6,10,26]
#
#
#
# Constraints:
#
#
# 1 <= label <= 10^6
#
#
import math


class Solution:
    def pathInZigZagTree(self, l):
        res = []
        rid = int(math.log(l, 2))
        while l > 1:
            res.append(l)
            nextl = l / 2 if l % 2 == 0 else (l - 1) / 2
            rid -= 1
            l = int(2 ** rid + (2 ** (rid + 1) - 1 - nextl))
        res.append(1)
        return res[::-1]


s = Solution()
print(s.pathInZigZagTree(14))
