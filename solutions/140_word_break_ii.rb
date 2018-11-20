# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word.Return all such possible sentences.
# Note:
#   The same word in the dictionary may be reused multiple times in the segmentation.
#   You may assume the dictionary does not contain duplicate words.
# Example 1:
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#  "cats and dog",
#  "cat sand dog"
# ]
# Example 2:
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#  "pine apple pen apple",
#  "pineapple pen apple",
#  "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#
#  https://leetcode.com/problems/word-break-ii/description/
require './aux.rb'

# @param {String} s
# @param {String[]} word_dict
# @return {String[]}
def word_break(s, word_dict)
  dict = {}
  backtracking(s, word_dict, dict)
end

def backtracking(s, word_dict, dict)
  return dict[s] if dict.key?(s)
  dict[s] = [] if dict[s].nil?
  word_dict.each do |w|
    dict[s] << s if w == s
    next unless s.start_with?(w)
    backtracking(s[w.length..-1], word_dict, dict).each do |ww|
      dict[s] << w + ' ' + ww
    end
  end
  dict[s]
end

s = 'pineapplepenapple'
word_dict = %w[apple pen applepen pine pineapple]

p word_break(s, word_dict)
