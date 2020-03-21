#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (40.74%)
# Total Accepted:    110.9K
# Total Submissions: 272.1K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
# Example:
#
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#
import bisect


class Solution:
    def countSmaller(self, nums):
        res = []
        tmp = []
        for n in nums[::-1]:
            idx = bisect.bisect_left(tmp, n)
            res.append(idx)
            bisect.insort(tmp, n)
        return res[::-1]


sol = Solution()
nums = [5, 2, 6, 1]
nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
# nums = [-1, -1]
print(sol.countSmaller(nums))
