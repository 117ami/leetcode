#
# @lc app=leetcode id=524 lang=ruby
#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (44.56%)
# Total Accepted:    34.9K
# Total Submissions: 78.3K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
#
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
#
# Example 1:
#
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
#
#
#
#
# Example 2:
#
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
#
#
#
# Note:
#
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
#
#
#
# @param {String} s
# @param {String[]} d
# @return {String}
def find_longest_word(s, d)
  d.sort { |a, b| [b.length, a] <=> [a.length, b] }.each { |t| return t if is_sub?(t, s) }
  ''
end

def is_sub?(t, s)
  return true if t.empty?
  return false if s.nil? || s.length < t.length

  j = 0
  j += 1 while j < s.length && s[j] != t[0]
  is_sub?(t[1..-1], s[j + 1..-1])
end

s = 'abpcplea'
d = %w[ale apple monkey plea blue]
# s = 'abpcplea'
# d = %w[a b c]
p find_longest_word(s, d)

d.each do |t|
  p [t, is_sub?(t, s)]
end
