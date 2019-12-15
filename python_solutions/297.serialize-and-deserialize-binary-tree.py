#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (44.08%)
# Total Accepted:    246.7K
# Total Submissions: 559.5K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# Example: 
#
#
# You may serialize the following tree:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
#
# as "[1,2,3,null,null,4,5]"
#
#
# Clarification: The above format is the same as how LeetCode serializes a
# binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
#
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
#
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        jobs = [root]
        res = []
        while len(jobs):
            r = jobs.pop(0)
            if r:
                res.append(r.val)
                jobs += [r.left, r.right]
            else:
                res.append(0.1)

        while res and res[-1] == 0.1:
            res.pop()

        return str(res).replace('0.1', 'null')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return 
        arr = []
        for i in data.replace('[', '').replace(']', '').split(','):
            arr.append(None if 'null' in i else int(i))

        children = 0

        i = 1
        jobs = [TreeNode(arr[0])]
        root = jobs[0]
        while i < len(arr):
            if children == 2:
                jobs.pop(0)
                children = 0

            if arr[i] is not None:
                c = TreeNode(arr[i])
                if children == 0:
                    jobs[0].left = c
                else:
                    jobs[0].right = c
                jobs.append(c)

            children += 1
            i += 1

        return root


            
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


s = Codec()
res = [1, 2, 3, 0.1, 0.1, 4, 5]
res = "[-1,0,-1]"
res = "[1,2,3,null,null,4,5]"
print(s.serialize(s.deserialize(res)))
# print(str(res).replace('0.1', 'null'))
# print("[1,2,3,null,null,4,5]".split(','))
