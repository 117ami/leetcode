#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (51.84%)
# Total Accepted:    6.2K
# Total Submissions: 12K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# 
# Return the length of the longest (contiguous) subarray that contains only
# 1s. 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
# 
# 
# Example 2:
# 
# 
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] is 0 or 1 
# 
# 
# 
# 
#
class Solution:
    def longestOnes(self, a, k):
    	i = 0
    	for j in range(len(a)):
    		k -= 1 - a[j]
    		if k < 0:
    			k += 1 - a[i]
    			i += 1
    	return j - i + 1

        

# a = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# k = 3

# print(Solution().longestOnes(a, k))
