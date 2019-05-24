#
# @lc app=leetcode id=1048 lang=ruby
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (44.33%)
# Total Accepted:    4.3K
# Total Submissions: 9.5K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# Given a list of words, each word consists of English lowercase letters.
#
# Let's say word1 is a predecessor of word2 if and only if we can add exactly
# one letter anywhere in word1 to make it equal to word2.  For example, "abc"
# is a predecessor of "abac".
#
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
# 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
# word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the
# given list of words.
#
#
#
# Example 1:
#
#
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
#
#
#
#
# Note:
#
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.
#
#
#
#
#
#
# @param {String[]} words
# @return {Integer}
def longest_str_chain(words)
  words.sort_by!(&:size)
  res = Hash.new(0)

  words.each do |w|
    maxlen = 0
    0.upto(w.size - 1).each do |i|
      left = i.zero? ? '' : w[0..i - 1]
      right = w[i + 1..w.size - 1]
      maxlen = [maxlen, res[left + right] + 1].max
    end
    res[w] = maxlen
  end
  res.values.max
  # res.map(&:size).max
end

words = %w[bdca b ba bca bda a]
p longest_str_chain(words)
