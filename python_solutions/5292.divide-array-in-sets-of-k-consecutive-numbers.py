#
# @lc app=leetcode id=5292 lang=python3
#
# [5292] Divide Array in Sets of K Consecutive Numbers
#
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
#
# algorithms
# Medium (39.56%)
# Total Accepted:    2.5K
# Total Submissions: 5.8K
# Testcase Example:  '[1,2,3,3,4,4,5,6]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into sets of k consecutive numbers
# Return True if its possible otherwise return False.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
#
#
# Example 2:
#
#
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and
# [9,10,11].
#
#
# Example 3:
#
#
# Input: nums = [3,3,2,2,1,1], k = 3
# Output: true
#
#
# Example 4:
#
#
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= nums.length
#
#


from collections import defaultdict, Counter


class Solution:
    def isPossibleDivide(self, ns, k):
        if k == 1: return True 
        if len(ns) % k > 0: return False 

        ns.sort()
        cter = Counter(ns)
        for n in ns:
            if cter[n] > 0:
                for i in range(k):
                    if cter[n+i] == 0:
                        return False
                    cter[n+i] -= 1
        
        return True 

s = Solution()
nums = [3,2,1,2,3,4,3,4,5,9,11, 9]
k = 3
print(s.isPossibleDivide(nums, k))