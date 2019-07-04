# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note:
#   The same word in the dictionary may be reused multiple times in the segmentation.
#   You may assume the dictionary does not contain duplicate words.
# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#             Note that you are allowed to reuse a dictionary word.
# Example 3:
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
#  https://leetcode.com/problems/word-break/description/
require './aux.rb'

# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}
def word_break(s, word_dict)
  dict = word_dict.zip([nil]).to_h
  res = Array.new(s.length + 1, false)
  res[0] = true
  1.upto(s.length).each do |idx|
    0.upto(idx).each do |jdx|
      if res[jdx] && dict.key?(s[jdx..idx - 1])
        res[idx] = true
        break
      end
    end
  end
  # p res
  res.last
end

def word_break2(s, word_dict)
  dict = {}
  backtracking(s, word_dict, dict)
end

def backtracking(s, word_dict, dict)
  return dict[s] if dict.key?(s)
  return true if word_dict.include?(s)
  word_dict.each do |w|
    if s.start_with?(w) && backtracking(s[w.length..-1], word_dict, dict)
      dict[s] = true
      return true
    end
  end
  dict[s] = false
  false
end

s = 'applepenapple'
word_dict = %w[apple pen]

# s = 'catsandog'
# word_dict = %w[cats dog sand and cat]

# s = 'leetcode'
# word_dict = %w[leet code]
p word_break(s, word_dict)
p word_break2(s, word_dict)
