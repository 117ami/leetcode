#
# @lc app=leetcode id=1090 lang=python3
#
# [1090] Largest Values From Labels
#
# https://leetcode.com/problems/largest-values-from-labels/description/
#
# algorithms
# Medium (53.75%)
# Total Accepted:    2.6K
# Total Submissions: 4.8K
# Testcase Example:  '[5,4,3,2,1]\n[1,1,2,2,3]\n3\n1'
#
# We have a set of items: the i-th item has value values[i] and label
# labels[i].
# 
# Then, we choose a subset S of these items, such that:
# 
# 
# |S| <= num_wanted
# For every label L, the number of items in S with label L is <= use_limit.
# 
# 
# Return the largest possible sum of the subset S.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit
# = 1
# Output: 9
# Explanation: The subset chosen is the first, third, and fifth item.
# 
# 
# 
# Example 2:
# 
# 
# Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit
# = 2
# Output: 12
# Explanation: The subset chosen is the first, second, and third item.
# 
# 
# 
# Example 3:
# 
# 
# Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit
# = 1
# Output: 16
# Explanation: The subset chosen is the first and fourth item.
# 
# 
# 
# Example 4:
# 
# 
# Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit
# = 2
# Output: 24
# Explanation: The subset chosen is the first, second, and fourth item.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= values.length == labels.length <= 20000
# 0 <= values[i], labels[i] <= 20000
# 1 <= num_wanted, use_limit <= values.length
# 
# 
# 
# 
# 
#
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:



s = Solution()


