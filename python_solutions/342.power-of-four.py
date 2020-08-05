#
# @lc app=leetcode id=342 lang=python
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (39.80%)
# Total Accepted:    101.4K
# Total Submissions: 254.7K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example 1:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: false
# 
# 
# Follow up: Could you solve it without loops/recursion?
#
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        0. num should be larger than 0
        1. There is only one '1' in bin repr of 4^n 
        2. 4^n - 1 = (2^n+1)(2^n-1).
        Among any 3 consecutive numbers, there must be one that is a multiple of 3
        Among (2^n-1), (2^n), (2^n+1), one of them must be a multiple of 3, 
        and (2^n) cannot be the one, therefore either (2^n-1) or (2^n+1) must be a multiple of 3, 
        and 4^n-1 must be a multiple of 3 as well.
        """
        
        return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0

