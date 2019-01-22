#
# @lc app=leetcode id=709 lang=ruby
#
# [709] To Lower Case
#
# https://leetcode.com/problems/to-lower-case/description/
#
# algorithms
# Easy (74.99%)
# Total Accepted:    52.8K
# Total Submissions: 70.4K
# Testcase Example:  '"Hello"'
#
# Implement function ToLowerCase() that has a string parameter str, and returns
# the same string in lowercase.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "Hello"
# Output: "hello"
# 
# 
# 
# Example 2:
# 
# 
# Input: "here"
# Output: "here"
# 
# 
# 
# Example 3:
# 
# 
# Input: "LOVELY"
# Output: "lovely"
# 
# 
# 
# 
# 
#
# @param {String} str
# @return {String}
def to_lower_case(str)
    str.downcase
end

str = 'LOVELY'
p to_lower_case(str)
