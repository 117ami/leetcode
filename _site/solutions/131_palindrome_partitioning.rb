# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# Example:
# Input:"aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
#
#  https://leetcode.com/problems/palindrome-partitioning/description/
require './aux.rb'

# @param {String} s
# @return {String[][]}
def partition(s)
  return [[]] if s.empty?
  return [[s]] if s.length == 1
  res = []
  0.upto(s.size - 1).each do |i|
    next unless s[0..i] == s[0..i].reverse
    partition(s[i + 1..-1]).each do |arr|
      arr.unshift(s[0..i])
      res << arr
    end
  end
  res
end

s = 'pppappbac'

p partition(s)
