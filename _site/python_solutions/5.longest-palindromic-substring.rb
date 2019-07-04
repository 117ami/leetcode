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
  0.upto(s.size).each do |i|
    j = i - 1
    i += 1 while i < s.size && s[i] == s[j + 1]
    k = i
    while j >= 0 && k < s.size && s[j] == s[k]
      j -= 1
      k += 1
    end
    if k - j - 1 > maxlen
      maxlen = k - j - 1
      start = j + 1
    end
  end
  # p start, maxlen
  s[start..start + maxlen - 1]
end

s = 'babad'
p longest_palindrome(s)
