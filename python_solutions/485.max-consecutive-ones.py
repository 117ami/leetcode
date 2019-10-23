#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (55.60%)
# Total Accepted:    156.2K
# Total Submissions: 280.5K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
#
# Example 1:
#
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
#
#
#
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#
#
#


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        res = curn = 0
        for e in nums:
            curn = 0 if e == 0 else curn + 1
            res = max(res, curn)
        return res
    
    # method 2: convert to string and split 
    def findMaxConsecutiveOnes_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max([len(s) for s in ''.join([str(i) for i in nums]).split('0')])




s = Solution()
nums = [1, 1, 0, 1, 1, 1]
print(s.findMaxConsecutiveOnes(nums))
