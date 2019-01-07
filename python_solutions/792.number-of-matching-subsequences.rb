#
# @lc app=leetcode id=792 lang=ruby
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (39.75%)
# Total Accepted:    14.8K
# Total Submissions: 37.2K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
#
#
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
#
#
# Note:
#
#
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
#
#
#
# @param {String} s
# @param {String[]} words
# @return {Integer}
def num_matching_subseq(s, words)
  words.group_by(&:itself).map { |k, v| is_subsequence(k, s) ? v.size : 0 }.reduce(:+)
end

def is_subsequence(s, t)
  return false if t.nil? || s.length > t.length
  return true if s.empty?

  j = 0
  j += 1 while j < t.length && t[j] != s[0]
  is_subsequence(s[1..-1], t[j + 1..-1])
end

words = %w[a bb acd ace bb ace]
s = 'abcde'

p num_matching_subseq(s, words)
