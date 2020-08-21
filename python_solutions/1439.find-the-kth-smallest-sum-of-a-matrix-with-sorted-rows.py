from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1439 lang=python3
#
# [1439] Find the Kth Smallest Sum of a Matrix With Sorted Rows
#
# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/description/
#
# algorithms
# Hard (56.18%)
# Total Accepted:    5.3K
# Total Submissions: 9.4K
# Testcase Example:  '[[1,3,11],[2,4,6]]\n5'
#
# You are given an m * n matrix, mat, and an integer k, which has its rows
# sorted in non-decreasing order.
#
# You are allowed to choose exactly 1 element from each row to form an array.
# Return the Kth smallest array sum among all possible arrays.
#
#
# Example 1:
#
#
# Input: mat = [[1,3,11],[2,4,6]], k = 5
# Output: 7
# Explanation: Choosing one element from each row, the first k smallest sum
# are:
# [1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
#
# Example 2:
#
#
# Input: mat = [[1,3,11],[2,4,6]], k = 9
# Output: 17
#
#
# Example 3:
#
#
# Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
# Output: 9
# Explanation: Choosing one element from each row, the first k smallest sum
# are:
# [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th
# sum is 9.
#
#
# Example 4:
#
#
# Input: mat = [[1,1,10],[2,2,9]], k = 7
# Output: 12
#
#
#
# Constraints:
#
#
# m == mat.length
# n == mat.length[i]
# 1 <= m, n <= 40
# 1 <= k <= min(200, n ^ m)
# 1 <= mat[i][j] <= 5000
# mat[i] is a non decreasing array.
#
#
#


class Solution_Naive:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        h = mat[0][:]
        for row in mat[1:]:
            h = sorted([i+j for i in row for j in h])[:k]
        return h[k-1]

        cnt = res = 0
        m, n = len(mat), len(mat[0])
        arr = [(sum(mat[i][0] for i in range(m)), (0,) * m)]
        heapq.heapify(arr)
        cc = set()

        while cnt < k:
            # print(arr)
            res, ids = heapq.heappop(arr)
            cnt += 1
            for i in range(m):
                if ids[i] < n - 1:
                    tuple_ids = tuple(e + 1 if j == i else e for j, e in enumerate(ids))
                    if tuple_ids not in cc:
                        cc.add(tuple_ids)
                        heapq.heappush(arr, (res + mat[i][tuple_ids[i]] - mat[i][tuple_ids[i]-1], tuple_ids))
                    # ids[i] -= 1
        return res


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def ordered_sums(rows):
            if len(rows) == 1:
                yield from rows[0]
            else:
                first, rest = rows[0], rows[1:]
                teed = itertools.tee(ordered_sums(rest), len(first))
                yield from heapq.merge( *( map(val.__add__, sums) for val, sums in zip(first, teed) ))
            
        return next(itertools.islice(ordered_sums(mat), k-1, None))


sol = Solution()
mat, k = [[1, 3, 11], [2, 4, 6]], 5
# mat, k = [[1,10,10],[1,4,5],[2,3,6]], 7
print(sol.kthSmallest(mat, k))
print(next(itertools.islice('ABCDEFG', 2, None)))
