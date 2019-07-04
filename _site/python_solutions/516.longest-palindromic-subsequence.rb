#
# @lc app=leetcode id=516 lang=ruby
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (46.30%)
# Total Accepted:    58.1K
# Total Submissions: 125.5K
# Testcase Example:  '"bbbab"'
#
#
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
#
#
# Example 1:
# Input:
#
# "bbbab"
#
# Output:
#
# 4
#
# One possible longest palindromic subsequence is "bbbb".
#
#
# Example 2:
# Input:
#
# "cbbd"
#
# Output:
#
# 2
#
# One possible longest palindromic subsequence is "bb".
#
#
# @param {String} s
# @return {Integer}
def longest_palindrome_subseq(s)
  return s.size if s == s.reverse

  cur = [0] * s.size
  (s.size - 1).downto(0).each do |i|
    pre = cur.dup
    cur[i] = 1
    (i + 1).upto(s.size - 1).each do |j|
      cur[j] = if s[i] == s[j]
                 2 + pre[j - 1]
               else
                 [cur[j - 1], pre[j]].max
               end
    end
  end
  cur.last
end

s = 'acc'
p longest_palindrome_subseq(s)
