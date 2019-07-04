#
# @lc app=leetcode id=258 lang=ruby
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (54.09%)
# Total Accepted:    238.5K
# Total Submissions: 440.7K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# Example:
# 
# 
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
# @param {Integer} num
# @return {Integer}
def add_digits(num)
    return 1 + [(num - 1) % 9, num - 1].min
end

p add_digits(0)
