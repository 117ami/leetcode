#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.97%)
# Total Accepted:    132.9K
# Total Submissions: 260.8K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: a = -2, b = 3
# Output: 1
# 
# 
# 
# 
#
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            print(a, b)
        # print(a, b)
        return a if a <= MAX else ~(a ^ mask)

        



s = Solution()
print(s.getSum(-1, 1))


