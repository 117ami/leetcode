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
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (53.61%)
# Total Accepted:    106.7K
# Total Submissions: 198.4K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
#
# An image is represented by a 2-D array of integers, each integer representing
# the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column)
# of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color as the starting pixel), and so on.  Replace the
# color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
#
# Example 1:
#
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels
# connected
# by a path of the same color as the starting pixel are colored with the new
# color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected
# to the starting pixel.
#
#
#
# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0  and 0 .
# The value of each color in image[i][j] and newColor will be an integer in [0,
# 65535].
#
#


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if newColor == image[sr][sc]: return image
        dirs = [-1, 0, 1, 0, -1]
        cc = set()
        q = deque([(sr, sc)])
        color = image[sr][sc]

        while len(q):
            b = q.popleft()
            if b in cc or image[b[0]][b[1]] != color: continue
            cc.add(b)
            image[b[0]][b[1]] = newColor
            for i in range(4):
                j, k = b[0] + dirs[i], b[1] + dirs[i + 1]
                if 0 <= j < len(image) and 0 <= k < len(image[0]):
                    q.append((j, k))
        return image


sol = Solution()
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(sol.floodFill(image, 1, 1, 2))
