# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def treeToList(self, root):
        """Encodes a tree to a list
        :type root: TreeNode
        :rtype: list[int]
        """
        jobs = [root]
        res = []
        while len(jobs):
            r = jobs.pop(0)
            if r:
                res.append(r.val)
                jobs += [r.left, r.right]
        return res

    def getAllElements(self, r1, r2):
        a = self.treeToList(r1) + self.treeToList(r2)
        a.sort()
        return a 

        