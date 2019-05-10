#
# @lc app=leetcode id=5 lang=ruby
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.16%)
# Total Accepted:    542.5K
# Total Submissions: 2M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#
# @param {String} s
# @return {String}
def longest_palindrome(s)
  return s if s == s.reverse

  start = 0
  maxlen = 1
  1.upto(s.size).each do |i|
    if i - maxlen >= 1 && s[i - maxlen - 1..i] == s[i - maxlen - 1..i].reverse
      start = i - maxlen - 1
      maxlen += 2
    elsif i - maxlen >= 0 && s[i - maxlen..i] == s[i - maxlen..i].reverse
      start = i - maxlen
      maxlen += 1
    end
  end
  # p start, maxlen
  s[start..start + maxlen - 1]
end

s = 'adam'
p longest_palindrome(s)
