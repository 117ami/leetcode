#
# @lc app=leetcode id=125 lang=ruby
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.83%)
# Total Accepted:    345.9K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#
# @param {String} s
# @return {Boolean}
def is_palindrome(s)
	s.gsub!(/[^0-9A-Za-z]+/, '')
	return true if s.nil?
	s.downcase!
	s == s.reverse
end

s = 'aa; 0; l : bbaa'
# s = 'p0P'
s = "A man, a plan, a canal: Panama"
s = ""
p is_palindrome(s)
