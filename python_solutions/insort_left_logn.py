import math


class TreeNode:
    def __init__(self, val, count=0, dup=1):
        self.val = val
        self.left = None
        self.right = None
        # Count of nodes with larger value than current node
        self.count = count
        self.dup = dup


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def binary_search_larger(val, node):
    ''' 1. Search for the smallest value that is larger than or equal to val.
        2. Insert val in a tree. 
    '''
    cnt = val
    if not node:
        return Node(val), math.inf
    elif node.val < val:
        child, cnt = binary_search_larger(val, node.right)
        node.right = child
    elif node.val > val:
        child, i32t = binary_search_larger(val, node.left)
        node.left = child
        cnt = min(node.val, i32t)
    return node, cnt


lis = [5, 6, 4, 3, 23, 3, 4, 9, 2, 3, 5]

import random
import bisect
N = 100_000


def b():
    lis = [random.randint(1, 100000) for i in range(N)]
    root = None
    for n in lis:
        root, m = binary_search_larger(n, root)


def a():
    lis = [random.randint(1, 100000) for i in range(N)]
    new = []
    for n in lis:
        i = bisect.bisect_left(new, n)
        bisect.insort_left(new, n)


from timeit import timeit
if __name__ == "__main__":
    print(timeit(stmt=a, number=1))
    print(timeit(stmt=b, number=1))

# def insert(val, node, presum=0):
#     smaller_than_self = 0
#     if not node:
#         node = TreeNode(val, 0, 1)
#         ans[i] = presum
#     elif val == node.val:
#         node.dup += 1
#         ans[i] = node.count + presum
#     elif val > node.val:
#         node.right = insert(val, node.right, i,
#                             presum + node.dup + node.count)
#     else:
#         node.count += 1
#         node.left = insert(val, node.left, i, presum)
#     return node

#     # root, ans = None, [0] * len(nums)
#     # for i in range(len(nums) - 1, -1, -1):
#     #     print(i, nums[i])
#     #     root = insert(nums[i], root, i, 0)
#     # return ans
