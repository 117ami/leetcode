from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right, insort_left
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007


#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (41.46%)
# Total Accepted:    134.3K
# Total Submissions: 323.4K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
#
# Example 1:
#
#
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
class TreeNode:
    def __init__(self, val, count=0, dup=1):
        self.val = val
        self.left = None
        self.right = None
        # Count of nodes with larger value than current node
        self.count = count
        self.dup = dup


class Solution:
    def on2_method(self, nums: List[int]) -> List[int]:
        # Brute force O(n**2) method
        n = len(nums)
        res = [0] * n
        i32sort = []
        for i, u in enumerate(nums[::-1]):
            idx = bisect_left(i32sort, u)
            res[n - i - 1] = idx
            insort_left(i32sort, u)
            print(u, i32sort, res)
        return res

    def bst_method(self, nums: List[int]) -> List[int]:
        # Binary search tree
        def insert(val, node, i, presum):
            if not node:
                node = TreeNode(val, 0, 1)
                ans[i] = presum
            elif val == node.val:
                node.dup += 1
                ans[i] = node.count + presum
            elif val > node.val:
                node.right = insert(val, node.right, i,
                                    presum + node.dup + node.count)
            else:
                node.count += 1
                node.left = insert(val, node.left, i, presum)
            return node

        root, ans = None, [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            print(i, nums[i])
            root = insert(nums[i], root, i, 0)
        return ans

    def countSmaller(self, nums: List[int]) -> List[int]:
        return self.bst_method(nums)
        # return self.on2_method(nums)
        n = len(nums)
        res = [0] * n
        """Indices of nums will be reordered by the value. For example,
        nums = [6, 4, 1, 8] with corresponding indices [0, 1, 2, 3]. This list 
        will be reordered in to [2, 1, 0, 3]. 
        
        The main ideas is using merge sort to reorder indices and update result 
        simultaneously, in detail:
        1. divide nums into two size-equal part: nums[:mid], nums[mid:]
        2. use mergesort to handle each part (global variable indices will be 
        updated in this procedure)
        3. update indices by comparing (nums[i], nums[j] for i in indices[:mid] 
        for j in indices[mid:]). Consider:
            1. nums[i] <= nums[j], then there is no need to update result
            2. otherwise, we've found a smaller number (nums[j]) on the right side
            of nums[i], we should increase res[i] by j - mid 
            (all numbers nums[k] for k in mid -> j are also smaller than nums[i])
        """
        indices = list(range(n))

        def mergesort(left, right):
            if right - left <= 1: return
            mid = (left + right) // 2
            mergesort(left, mid)
            mergesort(mid, right)
            tmp = []
            i, j = left, mid
            while i < mid or j < right:
                print(i, j, indices)
                if j == right or (i < mid
                                  and nums[indices[i]] <= nums[indices[j]]):
                    tmp.append(indices[i])
                    res[indices[i]] += j - mid
                    i += 1
                else:
                    tmp.append(indices[j])
                    j += 1
            print(len(tmp), len(indices[left:right]))
            indices[left:right] = tmp

        mergesort(0, n)
        return res


sol = Solution()
nums = [5, 2, 6, 1]
nums = [6, 4, 1, 8, 7, 5, 2, 9]
print(sol.countSmaller(nums))
