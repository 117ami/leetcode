# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold
# Medium (Difficulty)

# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
# Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
# It is guaranteed that there will be an answer.
#  
# Example 1:
# Example 2:
# Example 3:
#  
# Constraints:
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
# If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
#
# Input: nums = [2,3,5,7,11], threshold = 11
# Output: 3
#
# Input: nums = [19], threshold = 5
# Output: 4
#
# xxxxxxxxxx
# class Solution {
# public:
#     int smallestDivisor(vector<int>& nums, int threshold) {
#         
#     }
# };
import functools
import math
import bisect


class Solution:
    def cal_sum(self, nums, div):
        x, i, j, s = 1, 0, 0, 0
        while j < len(nums):
            j = bisect.bisect_right(nums, x * div)
            s += (j - i) * x
            i = j
            x += 1
        return s

    def smallestDivisor(self, ns, t):
        ns.sort()
        lo, hi = 1, 1e6
        while lo < hi:
            mi = (lo + hi) // 2
            if self.cal_sum(ns, mi) <= t:
                hi = mi
            else:
                lo = mi + 1
        return int(lo)


ns, t = [2, 3, 5, 7, 11], 11
ns, t = [1, 2, 5, 9], 6
ns, t = [19], 5
ns, t = [962551, 933661, 905225, 923035, 990560], 10
# ns, t = [16,79,6,43,53], 172
print(Solution().smallestDivisor(ns, t))
